import flask
from src.models.disaster_tweets_model import DisasterTweetsModel
import sys

# initialize our Flask application and the Keras model
app = flask.Flask(__name__)
model = DisasterTweetsModel()

@app.route("/predict", methods=["POST"])
def predict():
    texts = flask.request.json['data']
    result = model.predict(texts)
    sys.stdout.flush()
    return flask.jsonify(result.tolist())

if __name__ == "__main__":
	app.run()
