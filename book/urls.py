from django.urls import path
from .views import Hello,index,Authors,new_authors
urlpatterns = [
    path('hello/<str:first_name>/<int:age>/',Hello),
    path('html/',index),
    path('authors/',Authors),
    path('new_authors/',new_authors)
]
