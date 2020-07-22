import sklearn_crfsuite
import pandas as pd

class ner_model():
    def __init__(self, **kwargs):
        self.cnt = 0
        if 'model' in kwargs:
            self.model = joblib.load(kwargs.get('model'))
        else:
            self.model = sklearn_crfsuite.CRF(
                algorithm = 'l2sgd',
                c2=1,
                max_iterations=100,
                all_possible_transitions=True,
                verbose = True
            )
    def train(self):
        # data = pd.read_csv('data/labeled.csv')
        # data_x = data['text']
        # data_y = data['labels']
        # for i in range(len(data_x)):
        #     data_x[i] = extract_features(data_x[i].split())
        #     data_y[i] = data_y[i].split()
        data_x, data_y = self.load_data()
        for i in range(len(data_x)):
            data_x[i] = self.extract_features(data_x[i])
            data_y[i] = data_y[i]
        self.model.fit(data_x, data_y)

    def load_data(self):
        data = pd.read_csv('data/labeled.csv')
        data_x = data['text']
        data_y = data['labels']
        for i in range(len(data_x)):
            data_x[i] = data_x[i].split()
            data_y[i] = data_y[i].split()
        return data_x.to_list(), data_y.to_list()


    def predict(self, data_x):
        return self.model.predict_single(self.extract_features(data_x))

    def extract_features(self, sentence):
      sentence_features = []
      for j in range(len(sentence)):
        word_feat = {
                'word': sentence[j].lower(),
                'capital_letter': sentence[j][0].isupper(),
                'all_capital': sentence[j].isupper(),
                'isdigit': sentence[j].isdigit(),
                'word_before': sentence[j].lower() if j==0 else sentence[j-1].lower(),
                'word_after:': sentence[j].lower() if j+1>=len(sentence) else sentence[j+1].lower(),
                'BOS': j==0,
                'EOS': j==len(sentence)-1
        }
        sentence_features.append(word_feat)
      return sentence_features
