## Types of classifiers
For performing the experiments 3 types of models: BERT, LSTM and Bag of words model. Two sets of each models. First, they are trained on fox and Twitter dataset and then by using transfer learning to evaluate on movies utterances.
The performance of these models are also compared with a state-of-the art BERT-based classification model called [*HateXplain*](https://arxiv.org/abs/2012.10289)

### BERT
For BERT models we have used *TFBertForSequenceClassification* algorithm provided by [HuggingFace](https://huggingface.co/transformers/) and it is pretrained on bert-base-uncased. The hyperparameters used are mebntioned below.

* Learning rate: 3e-05
* Loss Function: Sparse categorical cross-entropy 
* Batch size: 32 
* Optimizer Algorithm: Adam optimizer

### LSTM
The LSTM based models are built using Keras library. However no pretrained word embedding were used for word representation. The owrd vectors were generated from scratch. The hyperparameters used are mebntioned below.

* Learning rate: 1e-03
* Loss Function: Categorical cross-entropy 
* Batch size: 32 
* Regularizer function: L2 regularizer
* Optimizer Algorithm: Adam optimizer

### Bag of Words(BoW)
Finally the experiments are also performed with a Pytorch Bag-of- Words model. The Hyperparameters are mentione as

* Learning rate: 1e-03
* Loss Function: Cross-entropy loss 
* Batch size: 32 
* Optimizer Algorithm: Adam optimizer


