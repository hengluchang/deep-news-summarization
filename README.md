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
0. Installed Python, Anaconda and Tensorflow
1. Create 3 folders named dataset, working_dir, and output. In this repo, I created subfolders as well to store files. 
```
mkdir -p dataset/10yapw working_dir/10yapw-512 output/10yapw-512
```
2. Parse dataset to headline.txt and article.txt and put them under dataset folder. If you are using English Gigaword, you may want to try using beautifulsoup (already in Anaconda) to parse SGML file. 
3. 
