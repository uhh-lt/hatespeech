import numpy as np
import tensorflow as tf
from sklearn.metrics import classification_report

from transformers import BertTokenizer, TFBertForSequenceClassification
from transformers import InputExample, InputFeatures




def convert_data_to_examples(train, DATA_COLUMN, LABEL_COLUMN):
    train_InputExamples = train.apply(
        lambda x: InputExample(guid=None,  # Globally unique ID for bookkeeping, unused in this case
                               text_a=x[DATA_COLUMN],
                               text_b=None,
                               label=x[LABEL_COLUMN]), axis=1)

    return train_InputExamples


def convert_examples_to_tf_dataset(examples, tokenizer, max_length=128):
    features = []  # -> will hold InputFeatures to be converted later

    for e in examples:
        # Documentation is really strong for this method, so please take a look at it
        input_dict = tokenizer.encode_plus(
            e.text_a,
            add_special_tokens=True,
            max_length=max_length,  # truncates if len(s) > max_length
            return_token_type_ids=True,
            return_attention_mask=True,
            pad_to_max_length=True,  # pads to the right by default # CHECK THIS for pad_to_max_length
            truncation=True
        )

        input_ids, token_type_ids, attention_mask = (input_dict["input_ids"],
                                                     input_dict["token_type_ids"], input_dict['attention_mask'])

        features.append(
            InputFeatures(
                input_ids=input_ids, attention_mask=attention_mask, token_type_ids=token_type_ids, label=e.label
            )
        )

    def gen():
        for f in features:
            yield (
                {
                    "input_ids": f.input_ids,
                    "attention_mask": f.attention_mask,
                    "token_type_ids": f.token_type_ids,
                },
                f.label,
            )

    return tf.data.Dataset.from_generator(
        gen,
        ({"input_ids": tf.int32, "attention_mask": tf.int32, "token_type_ids": tf.int32}, tf.int64),
        (
            {
                "input_ids": tf.TensorShape([None]),
                "attention_mask": tf.TensorShape([None]),
                "token_type_ids": tf.TensorShape([None]),
            },
            tf.TensorShape([]),
        ),
    )


def train_bert(df_train, df_test):
    model = TFBertForSequenceClassification.from_pretrained("bert-base-uncased",
                                                        trainable=True,
                                                        num_labels=3)
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    model.load_weights('training_1/cp.ckpt')
    train = df_train[['text', 'majority_answer']]
    train.columns = ['DATA_COLUMN', 'LABEL_COLUMN']

    test = df_test[['text', 'majority_answer']]
    test.columns = ['DATA_COLUMN', 'LABEL_COLUMN']

    DATA_COLUMN = 'DATA_COLUMN'
    LABEL_COLUMN = 'LABEL_COLUMN'

    train_InputExamples = convert_data_to_examples(train, DATA_COLUMN, LABEL_COLUMN)
    test_InputExamples = convert_data_to_examples(test, DATA_COLUMN, LABEL_COLUMN)

    train_data = convert_examples_to_tf_dataset(list(train_InputExamples), tokenizer)
    train_data = train_data.batch(32)

    # compile and fit
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=3e-5, epsilon=1e-08, clipnorm=1.0),
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=[tf.keras.metrics.SparseCategoricalAccuracy('accuracy')])

    model.fit(train_data, epochs=5)

    test_data = convert_examples_to_tf_dataset(list(test_InputExamples), tokenizer)
    test_data = test_data.batch(32)

    print('predicting')
    preds = model.predict(test_data)

    # classification
    return classification_report(test['LABEL_COLUMN'], np.argmax(preds[0], axis=1), output_dict=True)
