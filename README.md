# News summarization
News summarization using sequence to sequence model in TensorFlow.

# Introduction
This repo is a demonstration of abstractive summarization of news article exploiting [sequence to sequence model](https://www.tensorflow.org/tutorials/seq2seq/). This model is trainined on newswires from 1994-2004 Associated Press Worldstream (APW) from English gigaword second edition. The examples below were the results of the model trained using AWS EC2 g2.2xlarge instance for 10 epochs, which took around 20 hours. 

# Examples
News: President Vladimir Putin announced plans Monday for the Russian military to hold exercises in the former Soviet republic of Kyrgyzstan, the ITAR-Tass news agency reported. 
Actual headline: Russia plans military exercise in Kyrgyzstan
Predicted headline: Putin to launch military exercises in Kyrgyzstan

News: A roadside bomb killed five people Thursday near a shelter used as a police recruiting center in northeast Baghdad, police said.
Actual headline: Iraqi police: Bomb kills 5 near police recruiting center in northeast Baghdad
Predicted headline: URGENT Explosion kills five people in Baghdad
