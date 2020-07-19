#!/bin/bash
echo "$HEROKU_PASSWORD" | docker login -u "$HEROKU_USERNAME" --password-stdin registry.heroku.com
docker push mformihir/COVID-19-Predictive-Analysis