from django.shortcuts import render
from django.http import HttpResponse
from analysis.prediction.prediction import ml_algorithm

# Create your views here.
def index(request):
    return render(request, 'analysis/index.html')

def predict(request):
    user_input = request.GET.get('predict', False)
    output = ""
    output += "Calling testfile... \n"
    output += ml_algorithm()
    return HttpResponse(output)