from django.urls import path
from . import views

urlpatterns = [
    path('<str:topic>/',views.news,name='topic'),
    path('<int:num1>/<int:num2>', views.add),
]
