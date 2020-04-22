import flask
from src.models.disaster_tweets_model import DisasterTweetsModel
import sys
import os

def dvc_pull():
    os.system("git init") # The deployed app isn't a git repo but needs to be for dvc
    os.system("dvc pull prepare_train_submit.dvc")

# initialize our Flask application and the Keras model
app = flask.Flask(__name__)
dvc_pull()
model = DisasterTweetsModel()

@app.route("/predict", methods=["POST"])
def predict():
    texts = flask.request.json['data']
    result = model.predict(texts)
    return flask.jsonify(result.tolist())

if __name__ == "__main__":
    app.run()
