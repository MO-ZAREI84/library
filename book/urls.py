from django.urls import path
from .views import Hello,index
urlpatterns = [
    path('hello/<str:first_name>/<int:age>/',Hello),
    path('html/',index),
]
