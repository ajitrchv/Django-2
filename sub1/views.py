from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,Http404, HttpResponseRedirect
from django.template import Context, loader
from django.urls import reverse

def simple_view(request):
    # try:
        return render(request,'sub1/news_home.html')
    # except:
    #     return HttpResponse('Template not found!')