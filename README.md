# How Hateful are Movies? A study and prediction on Movie Subtitles
Use of Three different Models(BERT, LSTM and Bag of Words) which are trained and tested on movie utterances and using transfer learning by training on social media hate dataset.

## Abstract
In this research, we investigate techniques to detect hate speech in movies. We introduce a new dataset collected from subtitles of six movies, where each utterance is annotated either as hate, offensive or normal. We apply transfer learning techniques of domain adaptation and fine-tuning on existing social media datasets, namely from Twitter and Fox News. We evaluate different representations, i.e., Bag of Words (BoW), Long short-term memory (LSTM), and Bidirectional Encoder Representations from Transformers (BERT) on 11k movie subtitles. The BERT model obtained the best macro-averaged F1-score of 77%. Hence, we were able to show that transfer learning from the social media domain is effective in classifying hate and offensive speech in movies through subtitles.

## Folder Description
./Data                      --> contains the individual movie utterances files obtained after annotaion in MTurk. Also they are all combinded into a single file('all_movies.csv'). Apart from this the folder contains the social media hatespeech dataset(Fox News and Twitter).

./Models                    --> Contains the codes for all the classification models used

./Code For Annotations      --> Contains the codes for preprocessing the dataset, the raw subtitles and preparing them for annotations	


