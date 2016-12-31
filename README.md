## News summarization
News summarization using sequence to sequence model in TensorFlow.

## Introduction
This repo is a demonstration of abstractive summarization of news article exploiting Tensorflow [sequence to sequence model](https://www.tensorflow.org/tutorials/seq2seq/). This model is trainined on 1994-2004 Associated Press Worldstream (APW) newswires from English gigaword second edition. The examples below were the results of the model trained using AWS EC2 g2.2xlarge instance for 10 epochs, which took around 20 hours. 

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
0. Install Python, Anaconda and Tensorflow
1. Download newsum 
```
$ git clone https://github.com/hengluchang/newsum.git
```


2. Create 3 folders named dataset, working_dir, and output under the newsum folder. Create subfolders as well to work with different dataset. 
```
$ cd newsum
$ mkdir -p dataset/10yapw working_dir/10yapw output/10yapw
```


3. Obtain headline.txt and article.txt and put them under ./dataset/10yapw. If you are using English Gigaword, you may need to try using beautifulsoup (already in Anaconda) to parse SGML file first. 
4. Run 
