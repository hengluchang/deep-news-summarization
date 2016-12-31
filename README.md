## News summarization
News summarization using sequence to sequence model in TensorFlow.

## Introduction
This repository is a demonstration of abstractive summarization of news article exploiting TensorFlow [sequence to sequence model](https://www.tensorflow.org/tutorials/seq2seq/). This model incorporates attention mechanism and uses [LSTM cell](http://colah.github.io/posts/2015-08-Understanding-LSTMs/) as both encoder and decoder.
![image](https://github.com/hengluchang/newsum/blob/master/encoder-decoder_LSTM_attention.png)
This model is trained on 1994-2004 Associated Press Worldstream (APW) newswires from [English Gigaword second edition](https://catalog.ldc.upenn.edu/LDC2005T12). The examples below are based on the model trained on AWS EC2 g2.2xlarge instance for 10 epochs, which took around 20 hours. 

## Examples
### [News 1](https://www.highbeam.com/doc/1A1-D8SKOI7O0.html)
News: A roadside bomb killed five people Thursday near a shelter used as a police recruiting center in northeast Baghdad, police said.

Actual headline: Iraqi police: Bomb kills 5 near police recruiting center in northeast Baghdad

Predicted headline: URGENT Explosion kills five people in Baghdad

======================================
### [News 2](https://www.highbeam.com/doc/1A1-D8SNBQJ83.html)
News: The euro hit a record high against the dollar Monday in Asia as concerns over the U.S. subprime mortgage crisis remain a heavy weight on the greenback.

Actual headline: Euro hits record high versus dollar in Asian trading

Predicted headline: Euro hits record high against dollar

## How to run
### Pre-req
- Install Python, Anaconda, and TensorFlow
- Download newsum 
```
$ git clone https://github.com/hengluchang/newsum.git
```

- Create three folders named "dataset", "working_dir", and "output" under the newsum folder. You can create subfolders as well to work with different dataset. 
```
$ cd newsum
$ mkdir -p dataset/10yapw working_dir/10yapw output/10yapw
```

- You can obtain English Gigaword from university libraries and use Beautiful Soup 4 (already in Anaconda) to parse SGML file. Generate article.txt with each line as the first sentence of each articles as well as its corresponding headlines in headline.txt and put them under ./dataset/10yapw. You can use your own dataset as well for article.txt and headline.txt. 
- Run split_data.py to split the dataset into training, evaluation, and testing sets. train_enc.txt, eval_enc.txt, test_enc, train_dec.txt, eval_dec.txt, and test_dec.txt total of six files will be generated under ./dataset/10yapw. 
```
$ python split_data.py
```

### Training
- Set "mode = train" in seq2seq.ini file. 
- Run execute.py. This will generate vocab80000_enc.txt, vocab80000_dec.txt, and checkpoint data under ./working_dir/10yapw. If you use your own dataset, optimizing bucket sizes to minimize padding in execute.py file will give you better results. Also, keep training the model until the [preplexity](https://www.youtube.com/watch?v=OHyVNCvnsTo) of the evaluation sets are under 10.  
```
$ python execute.py
```

### Testing
- Set "mode = test" in seq2seq.ini file. 
- Run execute.py. This will read the model parameters (seq2seq.ckpt-XXXXX) into your model and generate predicted_test_headline.txt under ./output/10yapw. 

```
$ python execute.py
```

- Run evaluation.py to get [BLEU](https://en.wikipedia.org/wiki/BLEU) scores between actual headlines and predicted headlines. 
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
