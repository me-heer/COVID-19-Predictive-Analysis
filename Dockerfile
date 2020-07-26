FROM python:3.7
ENV PYTHONUNBUFFERED 1

WORKDIR /covid_analysis
ADD ./requirements.txt /covid_analysis/requirements.txt
RUN pip install -r requirements.txt
ADD . /covid_analysis

CMD [ "python", "manage.py", "runserver" ]