## News summarization
News summarization using sequence to sequence model in TensorFlow.

## Introduction
This repo is a demonstration of abstractive summarization of news article exploiting Tensorflow [sequence to sequence model](https://www.tensorflow.org/tutorials/seq2seq/). This model is trainined on 1994-2004 Associated Press Worldstream (APW) newswires from English Gigaword second edition. The examples below were the results based on the model trained using AWS EC2 g2.2xlarge instance for 10 epochs, which took around 20 hours. 

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
======================================

0. Install Python, Anaconda and Tensorflow
1. Download newsum 

```
$ git clone https://github.com/hengluchang/newsum.git
```

2. Create three folders named dataset, working_dir, and output under the newsum folder. Create subfolders as well to work with different dataset. 

```
$ cd newsum
$ mkdir -p dataset/10yapw working_dir/10yapw output/10yapw
```

3. Obtain English Gigaword from university libraries, and use Beautiful Soup 4 (already in Anaconda) to parse SGML file. Generate article.txt with each line as the first sentence of each articles as well as its corresponding headlines to store in headline.txt and put them under ./dataset/10yapw. You can use your own dataset as well for article.txt and headline.txt. 
4. Run split_data.py to split the dataset into training, evaluation, and testing sets. train_enc.txt, eval_enc.txt, test_enc, train_dec.txt, eval_dec.txt, and test_dec totoal of six files will be generated under ./dataset/10yapw. 
```
$ python split_data.py
```

### Training
======================================

1. Set "mode = train" in seq2seq.ini file. 
2. Run execute.py. This will generate vocab80000_enc.txt, vocab800000_dec.txt, and checkpoint data under ./working_dir/10yapw. If you use your own dataset, optimizing bucket sizes and numbers to minimize padding in execute.py file will give you better results. Also, keep training the model until the preplexity of the evaluation sets are under 10.  
```
$ python execute.py
```

### Testing
======================================

1. Set "mode = test" in seq2seq.ini file. 
2. Run execute.py. This will read the model parameters (seq2seq.ckpt-XXXXX) into your model and generate predicted_test_headline.txt under ./output/10yapw. 

```
$ python execute.py
```

3. Run evaluation.py to get BLEU scores between actual headlines and predicted headlines. 
```
$ python evaluation.py
```


### Interactive testing
======================================

1. Set "mode = interactive" in seq2seq.ini file.
2. Run execute.py. This will read the model parameters (seq2seq.ckpt-XXXXX) into your model and ask user for an input. 
```
$ python execute.py
```

## References
- [Sequence-to-Sequence Models](https://www.tensorflow.org/tutorials/seq2seq/)
- [Chatbots with Seq2Seq](http://suriyadeepan.github.io/2016-06-28-easy-seq2seq/)
- [Speakeasy chatbot](http://lauragelston.ghost.io/speakeasy/)
- [Generating News Headlines with Recurrent Neural Networks](https://arxiv.org/abs/1512.01712)
- [Evaluation and preplexity](https://www.youtube.com/watch?v=OHyVNCvnsTo)
