
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hi, This is meant to be home')
