from django.urls import path
from .views import Hello
urlpatterns = [
    path('hello/<str:first_name>/<int:age>/',Hello)
]
