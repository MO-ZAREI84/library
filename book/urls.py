from django.urls import path
from .views import Hello,index,Authors
urlpatterns = [
    path('hello/<str:first_name>/<int:age>/',Hello),
    path('html/',index),
    path('authors/',Authors)
]
