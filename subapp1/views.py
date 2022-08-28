from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,Http404, HttpResponseRedirect
from django.template import Context, loader
from django.urls import reverse

articles = {
    "sports":"This is Sports Page!",
    "finance":"This is Finance Page!",
    "politics":"This is politics Page!"
}

def news_home(request):
     try:
        template = loader.get_template('C:/Users/ajith/Desktop/Notes/Django/app2/subapp1/news_home.html')
        return HttpResponse(template.render())
     except:
         return HttpResponse("Hi, Template not available!")

def news(request,topic):
    try:
        result = articles[topic]
        return HttpResponse(result)
    except:
        raise Http404('404! Page not Found!')

#----> Conversion method
def page_num(request,num):
    try:
        topiclist =  list(articles.keys())
        topic = topiclist[num]
        
        #---> using reverse method lookup
        webpage = reverse('topic-page',args=[topic])
        #print(webpage)
        return HttpResponseRedirect(webpage)
    except:
        raise Http404('404! Page Not Found!')
    

def page_home(request):
    return HttpResponseRedirect(reverse('page-home'))
    