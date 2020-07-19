#!/bin/bash
echo "$HEROKU_PASSWORD" | docker login -u "$HEROKU_USERNAME" --password-stdin registry.heroku.com
docker tag covid-19-predictive-analysis_web registry.heroku.com/covid-analysis-mformihir/web
docker push registry.heroku.com/covid-analysis-mformihir/web