#!/bin/bash
echo "$HEROKU_PASSWORD" | docker login -u "$HEROKU_USERNAME" --password-stdin registry.heroku.com
docker tag covid-19-predictive-analysis_web $DOCKER_USERNAME/covid-19-predictive-analysis_web:latest
docker push mformihir/covid-19-predictive-analysis_web:latest