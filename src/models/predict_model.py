import click
from src.models.disaster_tweets_model import DisasterTweetsModel

@click.command()
@click.argument("text")
def predict(text):
    model = DisasterTweetsModel()
    print(model.predict([text])[0][0])

if __name__ == '__main__':
    predict()
