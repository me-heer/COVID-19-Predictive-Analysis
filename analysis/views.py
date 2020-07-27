from django.shortcuts import render
from django.http import HttpResponse
from analysis.prediction.prediction import ml_algorithm
import updater.update as up
from datetime import datetime, timedelta

# Create your views here.
def index(request):
    return render(request, 'analysis/index.html')

def predict(request):
    user_input = request.GET.get('predict', False)
    output = ""
    output += "Calling testfile... \n"
    output += ml_algorithm()
    return HttpResponse(output)

def update(request):
    last_updated_date = datetime(2020, 7, 22) #you should store this in the database
    output = up.update_models(last_updated_date)
    return HttpResponse(output)