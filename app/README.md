# NLP Disaster Tweets Web app

This is an HTTP API to run model inference. The web app is powered by Flask.

## Running the web app

From the project root:

```
honcho -f Procfile.dev start
```

If the source code (``*.py` files) is updated, the app is reloaded automatically in development mode.

## Example Usage

```
curl --location --request POST 'http://localhost:5000/predict' \
--header 'Content-Type: application/json' \
--data-raw '{"data":["Theyd probably still show more life than Arsenal did yesterday, eh? EH?","Just happened a terrible car crash"]}'
```

```
[
  [
    0.1800956279039383
  ],
  [
    0.7395803928375244
  ]
]
```

* 0 - Not a disaster
* 1 - Disaster

## Deploying to Heroku

From the project root:

```
APP_NAME=nlp-disaster-tweets
heroku create -a $APP_NAME
heroku buildpacks:add -a $APP_NAME https://github.com/heroku/heroku-buildpack-multi-procfile
heroku buildpacks:add heroku/python
heroku config:set PROCFILE=app/Procfile
git push heroku master
```

Substitute `nlp-disaster-tweets` with your own unique application name.
