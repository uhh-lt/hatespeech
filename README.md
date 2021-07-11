# How Hateful are Movies? A study and prediction on Movie Subtitles :speaking_head:
Use of Three different Models(BERT, LSTM and Bag of Words) which are trained and tested on movie utterances and using transfer learning by training on social media hate dataset.

## Abstract
In this research, we investigate techniques to detect hate speech in movies. We introduce a new dataset collected from subtitles of six movies, where each utterance is annotated either as hate, offensive or normal. We apply transfer learning techniques of domain adaptation and fine-tuning on existing social media datasets, namely from Twitter and Fox News. We evaluate different representations, i.e., Bag of Words (BoW), Long short-term memory (LSTM), and Bidirectional Encoder Representations from Transformers (BERT) on 11k movie subtitles. The BERT model obtained the best macro-averaged F1-score of 77%. Hence, we were able to show that transfer learning from the social media domain is effective in classifying hate and offensive speech in movies through subtitles.

## Folder Description
```
./Data                  --> contains social media hatespeech dataset(Fox News and Twitter), individual movie utterances files as well as combinded into a single file('all_movies.csv') obtained after annotaion in MTurk.

./Models                --> Contains the codes for all the classification models used

./Code For Annotations  --> Contains the codes for preprocessing the dataset, the raw subtitles and preparing them for annotations	
```

## Sections
[Data](https://github.com/uhh-lt/hatespeech/blob/main/Data/README.md): This contains the different types of datasets used in the experiments and also describes their annotation process

[Models](https://github.com/uhh-lt/hatespeech/blob/main/Models/README.md): This folder contains the classification models used to classify the movies


[Annotations](https://github.com/uhh-lt/hatespeech/blob/main/Code For Annotations/README.md): This folder contains the annotation process and the pre-processing and cleaning of the datasets
