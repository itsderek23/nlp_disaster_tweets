import keras
from keras.preprocessing.sequence import pad_sequences
import pickle

MAX_LEN=50


class DisasterTweetsModel:

    def __init__(self):
        self.model = keras.models.load_model("models/model.h5")
        with open('models/tokenizer.pickle', 'rb') as handle:
            self.tokenizer = pickle.load(handle)

    def predict(self,texts):
        # TODO NEXT - pre-process the texts
        sequences = self.tokenizer.texts_to_sequences(texts)
        processed_texts = pad_sequences(sequences,maxlen=MAX_LEN,truncating='post',padding='post')
        return self.model.predict(processed_texts)
