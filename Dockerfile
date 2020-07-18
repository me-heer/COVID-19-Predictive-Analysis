FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN mkdir /covid_analysis
WORKDIR /covid_analysis/
COPY requirements.txt /covid_analysis/
RUN pip install -r requirements.txt

COPY . .