[![Build Status](https://travis-ci.com/mformihir/COVID-19-Predictive-Analysis.svg?token=SHCD8xTDhUdFdgg3RAu9&branch=master)](https://travis-ci.com/mformihir/COVID-19-Predictive-Analysis)
# Running the server:
- cd into the root directory of the project.

`python manage.py runserver`

- The project uses MySQL Database by default. By default USER: 'root', PASSWORD: 'root'.
- Change your database use settings accordingly in `$BASE_DIR/settings.py`
- You will also need other database drivers depending on the database you are using. MySQL requires DB API Driver.
- Install DB API Driver: `pip install mysqlclient`
- For other databases refer to: https://docs.djangoproject.com/en/3.0/ref/databases/

# Requirements:
- Facebook Prophet (https://facebook.github.io/prophet/docs/installation.html)
- Pystan (Prophet dependency)
- plotly
- Pandas
- APScheduler

