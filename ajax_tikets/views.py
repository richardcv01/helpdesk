from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('Hello World!')

#def home(request):
 #   return render_to_response('index.html', {'variable': 'world'})

# Create your views here.
