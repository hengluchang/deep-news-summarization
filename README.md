[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8561a549b3d44399811d008c328aa738)](https://www.codacy.com/app/hengluchang/newsum?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=hengluchang/newsum&amp;utm_campaign=Badge_Grade)

## News summarization
News summarization using sequence to sequence model in TensorFlow.

## Introduction
This repository is a demonstration of abstractive summarization of news article exploiting TensorFlow [sequence to sequence model](https://www.tensorflow.org/tutorials/seq2seq/). This model incorporates attention mechanism and uses [LSTM cell](http://colah.github.io/posts/2015-08-Understanding-LSTMs/) as both encoder and decoder.

![](https://github.com/hengluchang/newsum/blob/master/seq2seq.PNG)

This model is trained on one million Associated Press Worldstream news stories from [English Gigaword second edition](https://catalog.ldc.upenn.edu/LDC2005T12). The examples below are based on the model trained on AWS EC2 g2.2xlarge instance for 10 epochs, which took around 20 hours.

For more detailed information, please see our project research paper: [Headline Generation Using Recurrent Neural Network](https://github.com/hengluchang/newsum/blob/master/headline-generation-recurrent.pdf).

## Examples

### [News 1](https://www.highbeam.com/doc/1A1-D8SKOI7O0.html)
News: A roadside bomb killed five people Thursday near a shelter used as a police recruiting center in northeast Baghdad, police said.

Actual headline: Iraqi police: Bomb kills 5 near police recruiting center in northeast Baghdad

Predicted headline: URGENT Explosion kills five people in Baghdad

### [News 2](https://www.highbeam.com/doc/1A1-D8SNBQJ83.html)
News: The euro hit a record high against the dollar Monday in Asia as concerns over the U.S. subprime mortgage crisis remain a heavy weight on the greenback.

Actual headline: Euro hits record high versus dollar in Asian trading

Predicted headline: Euro hits record high against dollar

## How to run
For demonstration, we use the [sample file](https://catalog.ldc.upenn.edu/desc/addenda/LDC2003T05.gz) (a very small portion of English Gigaword) from LDC as our dataset to train our model. If you want to reproduce the results like the above examples, larger training set is necessary.  You can download the trained model parameters which was trained on a larger portion on Gigaword by following the instructions in the *Download vocabs and trained model parameters* section below. The whole English Gigaword can be obtained from university libraries.

### Pre-req
- Install Python 3
- Download deep-news-summarization

```
$ git clone https://github.com/hengluchang/deep-news-summarization.git
```

- Install TensorFlow 0.12, pandas, Numpy, nltk, and requests
```
$ pip install -r requirements.txt
```

- Create two folders named "working_dir" and "output" under the deep-news-summarization folder.

```
$ cd deep-news-summarization
$ mkdir -p working_dir output
```

### Download vocabs and trained model parameters
- Run download_vocabs_and_trained_params.py file. This will download encoder and decoder vocabularies
and trained model parameters to working_dir folder.

```
$ python download_vocabs_and_trained_params.py ./working_dir
```
- Go to Interactive testing section below to reproduce the results as the examples above.

### Train your own summarizer
- Set "mode = train" in seq2seq.ini file.
- Run split_data.py file to split the dataset into training, evaluation, and testing sets. train_enc.txt, eval_enc.txt, test_enc, train_dec.txt, eval_dec.txt, and test_dec.txt total of six files will be created under ./dataset.

```
$ python split_data.py
```

- Run execute.py file. This will create vocab80000_enc.txt, vocab80000_dec.txt, and checkpoint data under ./working_dir. If you use your own dataset, optimizing bucket sizes to minimize padding in execute.py file can help to get better results. Also, keep training the model until the [preplexity](https://www.youtube.com/watch?v=OHyVNCvnsTo) of the evaluation sets are under 10 for better performances.  

```
$ python execute.py
```

### Testing
- Set "mode = test" in seq2seq.ini file.
- Run execute.py file. This will read the model parameters (seq2seq.ckpt-XXXXX) into your model and create predicted_test_headline.txt under ./output.

```
$ python execute.py
```

- Run evaluation.py file to get [BLEU](https://en.wikipedia.org/wiki/BLEU) scores between actual headlines and predicted headlines. This will create BLEU.txt file.

```
$ python evaluation.py
```


### Interactive testing
- Set "mode = interactive" in seq2seq.ini file.
- Run execute.py. This will read the model parameters (seq2seq.ckpt-XXXXX) into your model and ask user for an input.

```
$ python execute.py
```

## References
- [Sequence-to-Sequence Models](https://www.tensorflow.org/tutorials/seq2seq/): TensorFlow's tutorial using seq2seq_model.py.
- [Chatbots with Seq2Seq](http://suriyadeepan.github.io/2016-06-28-easy-seq2seq/): I adpoted most of the code from this blog.
- [Speakeasy chatbot](http://lauragelston.ghost.io/speakeasy/): A blog with benchmarked training step-time using various computing engines.
- [Generating News Headlines with Recurrent Neural Networks](https://arxiv.org/abs/1512.01712): A related work in generating news haedlines.
- [Evaluation and preplexity](https://www.youtube.com/watch?v=OHyVNCvnsTo): A youtube video explaining preplexity.
- [Understanding LSTM Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/): A blog explaning LSTM.
