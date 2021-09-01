There are 3 models used for performing the experiment. The results were compared with the benchmark HateXplain model.
## Model Folder Description
```
./LSTM        --> contains the BI-LSTM models to capture sequential nature of the movies.

./BoW         --> Contains the BoW models used as a baseline model

./BERT        --> Contains the BERT models due to its recent success in NLP studies and to capture contextual representation in utterances

./HateXplain  --> Contains the HateXplain model trained and classified for movies dataset
```
Each of the above folders has the models performing In-Domain(training and prediction on twitter, Fox), Domain adaptation(training on twitter, Fox and prediction with movies), In-Domain movies(training and prediction with movies dataset with 6 fold CV). Fine tuning(training with twitter and fine tuning with movies) only performed for BERT model.

For the further details about models and the experiments check out our paper
```
@article{von2021hateful,
  title={How Hateful are Movies? A Study and Prediction on Movie Subtitles},
  author={von Boguszewski, Niklas and Moin, Sana and Bhowmick, Anirban and Yimam, Seid Muhie and Biemann, Chris},
  journal={arXiv preprint arXiv:2108.10724},
  year={2021}
}
```
