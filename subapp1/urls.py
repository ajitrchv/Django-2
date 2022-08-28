from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home),
    path('<int:num>', views.page_num),
    path('<str:topic>/',views.news,name='topic'),
]
