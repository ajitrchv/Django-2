from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,Http404

articles = {
    "sports":"This is Sports Page!",
    "finance":"This is Finance Page!",
    "politics":"This is politics Page!"
}

def news(request,topic):
    try:
        result =articles[topic]
        return HttpResponse(result)
    except:
        raise Http404('404! Page not Found!')

def add(request, num1, num2):
    result = num1+num2
    return HttpResponse(str(result))
