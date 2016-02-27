from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_world(request):
    #return render(request, 'try/hello.html', {})
    return HttpResponse('<h1>Hello World!</h1>')