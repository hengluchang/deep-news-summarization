from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging
from flask import Flask, render_template, request, make_response
app = Flask(__name__)

import math
import random
import time
import sys
import os

import numpy as np
#from six.moves import xrange  # pylint: disable=redefined-builtin
import tensorflow as tf

import data_utils
import seq2seq_model

from configparser import ConfigParser # In Python 3, ConfigParser has been renamed to configparser for PEP 8 compliance.

gConfig = {}

def get_config(config_file='seq2seq.ini'):
    parser = ConfigParser()
    parser.read(config_file)
    # get the ints, floats and strings
    _conf_ints = [ (key, int(value)) for key,value in parser.items('ints') ]
    _conf_floats = [ (key, float(value)) for key,value in parser.items('floats') ]
    _conf_strings = [ (key, str(value)) for key,value in parser.items('strings') ]
    return dict(_conf_ints + _conf_floats + _conf_strings)

_buckets = [(30, 10), (30, 20), (40, 10), (40, 20), (50, 20)]  # 10y apw

def create_model(session, forward_only):
    global model
    """Create model and initialize or load parameters"""
    model = seq2seq_model.Seq2SeqModel( gConfig['enc_vocab_size'], gConfig['dec_vocab_size'], _buckets, gConfig['hidden_units'], gConfig['num_layers'], gConfig['max_gradient_norm'], gConfig['batch_size'], gConfig['learning_rate'], gConfig['learning_rate_decay_factor'], forward_only=forward_only)

    ckpt = tf.train.get_checkpoint_state(gConfig['working_directory'])
    if ckpt and tf.gfile.Exists(ckpt.model_checkpoint_path):
        print("Reading model parameters from %s" % ckpt.model_checkpoint_path)
        model.saver.restore(session, ckpt.model_checkpoint_path)
    # return model

def decode_input(sentence):
    # Load vocabularies.
    enc_vocab_path = os.path.join(gConfig['working_directory'],"vocab%d_enc.txt" % gConfig['enc_vocab_size'])
    dec_vocab_path = os.path.join(gConfig['working_directory'],"vocab%d_dec.txt" % gConfig['dec_vocab_size'])

    enc_vocab, _ = data_utils.initialize_vocabulary(enc_vocab_path)
    _, rev_dec_vocab = data_utils.initialize_vocabulary(dec_vocab_path)

    # Get token-ids for the input sentence.
    token_ids = data_utils.sentence_to_token_ids(sentence, enc_vocab)
    # Which bucket does it belong to? And place the sentence to the last bucket if its token length is larger then the bucket length.
    bucket_id = min([b for b in range(len(_buckets)) if _buckets[b][0] > len(token_ids)] + [len(_buckets)-1])
    # Get a 1-element batch to feed the sentence to the model.
    encoder_inputs, decoder_inputs, target_weights = model.get_batch(
      {bucket_id: [(token_ids, [])]}, bucket_id)
    # Get output logits for the sentence.
    _, _, output_logits = model.step(sess, encoder_inputs, decoder_inputs,
                                   target_weights, bucket_id, True)
    # This is a greedy decoder - outputs are just argmaxes of output_logits.
    outputs = [int(np.argmax(logit, axis=1)) for logit in output_logits]

    # If there is an EOS symbol in outputs, cut them at that point.
    if data_utils.EOS_ID in outputs:
        outputs = outputs[:outputs.index(data_utils.EOS_ID)]
        # Print out headline sentence corresponding to outputs.
    result = " ".join([tf.compat.as_str(rev_dec_vocab[output]) for output in outputs])
    return result

def readfile():
    global sess
    sess = tf.Session()

    # Create model and load parameters.
    create_model(sess, True)
    model.batch_size = 1  # We decode one sentence at a time.

    print("done with read file.")


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', result='')

    if request.method == 'POST':
        if request.form['title']:
            title = request.form['title']

        read_data = decode_input(title)
        return render_template('index.html', result=read_data)
@app.before_first_request
def setup_logging():
    if app.debug:
        # In production mode, add log handler to sys.stderr.
        app.logger.addHandler(logging.StreamHandler())
        app.logger.setLevel(logging.INFO)

if __name__ == "__main__":
    # get configuration from seq2seq.ini
    gConfig = get_config()
    readfile()
    app.run(port = 8000, debug=True)
