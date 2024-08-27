from django.urls import path
from .views import Hello,index,Authors,new_authors,Author_list,HelloView
urlpatterns = [
    path('hello/<str:first_name>/<int:age>/',Hello),
    path('html/',index),
    path('authors/',Authors),
    path('new_authors/',new_authors),
    path('authorlist/',Author_list),
    path('cvb', HelloView.as_view())
    # path('authorlist/<int:id>/',author_detail)
]
