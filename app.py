import os
# Libs to render front-end and communication front-back-end
from flask import Flask, render_template, request
import json
# Libs for machine learning (active learning annotation)
import sklearn_crfsuite
import pandas as pd
import joblib
import ner


model = []
app = Flask(__name__)

# Renders front-end (working) ----------------------------------------------------------------
@app.route("/", methods=["GET"])
def home():
    return render_template("anno_tool.html", py_txt="HELLO WORLD!", py_txt2="HEYO")

# Retrieves labels of annotated text (working) ------------------------------------------------
@app.route('/postmethod', methods = ['POST'])
def get_post_javascript_data():
    jsdata = request.form['javascript_data']
    jsdata = json.loads(jsdata)
    switch_sets(jsdata)
    return "done"

def switch_sets(annotations):
    # switch text from unlabeled.csv to labeled.csv along with annotated labels
    # Turn labels from list of lists into a single list
    annotations = [item for sublist in annotations for item in sublist]
    # load unlabeled data
    data = pd.read_csv('data/unlabeled.csv')
    # Append text and retrieved labels to labeled.csv
    a = pd.DataFrame(data={'text': data['text'][0], 'labels': [' '.join(annotations)]})
    if(os.path.isfile("data/labeled.csv")):
        a.to_csv('data/labeled.csv', mode='a', header=False)
    else:
        a.to_csv('data/labeled.csv', mode='a', header=True)
    # Drop first text (row) from unlabeled.csv (as it was already labeled)
    data = data.drop(0, axis=0)
    data.to_csv('data/unlabeled.csv', columns=['text'])
    # Increment counter and if cnt==2 retrain model (DELETE THIS IF retrain_NER() is functional) ############################# DELETE ################
    # model.cnt += 1
    # if model.cnt == 2:
    #     model.train()
    #     model.cnt = 0

# Receives command to load next text to be annotated ----------------------------------------
@app.route('/getpythondata')
def get_python_data():
    data = pd.read_csv('data/unlabeled.csv')
    pythondata = data['text'][0].split()
    pythonlabels = get_label_suggestions(pythondata)
    python_data = [pythondata, pythonlabels]
    return json.dumps(python_data)

def get_label_suggestions(sent):
    if not model.model.tagger_:
        print("ALL Osssssss")
        labels = ["O" for i in range(len(sent))]
    else:
        print("SUGGESTED LABELS")
        labels = model.predict(sent)
    return labels

# Delete text entry -------------------------------------------------------------------------
@app.route('/deleteTextEntry', methods = ['POST'])
def delete_text_entry():
    print("DELETE_TEXT_ENTRY")
    data = pd.read_csv('data/unlabeled.csv')
    data[1:].to_csv('data/unlabeled.csv', columns=['text'])
    # get_python_data()
    return "done"

# Train suggestions ner_model ---------------------------------------------------------------
@app.route('/retrainNER', methods = ['POST'])
def retrain_NER():
    print("RETRAIN MODEL")
    if(os.path.isfile("data/labeled.csv")):
        model.train()
        data = pd.read_csv('data/unlabeled.csv')
        get_python_data()
    return "done"

# MAIN ---------------------------------------------------------------------------------------
if __name__ == "__main__":
    model = ner.ner_model()
    app.run(debug=True)
