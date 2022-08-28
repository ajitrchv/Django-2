from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home),
    path('page_home',views.page_home),
    path('<int:num>', views.page_num, name='num-page'),
    path('<str:topic>/',views.news,name='topic-page'),
]
