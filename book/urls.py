from django.urls import path
from .views import Hello,index,Authors,new_authors,Author_list,HelloView,AuthorListView,library,user_list,register,login,change_password,HelloView2
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('hello/<str:first_name>/<int:age>/',Hello),
    path('html/',index),
    path('authors/',Authors),
    path('new_authors/',new_authors),
    path('authorlist/',Author_list),
    path('cvb', HelloView.as_view()),
    path('Author_list_view',AuthorListView.as_view()),
    # path('library/<int=id>/',library)
    # path('authorlist/<int:id>/',author_detail)
    path('users/',user_list),
    path('register/',register),
    path('login/',login),
    path('change-password/', change_password),
    path('hello/',HelloView2.as_view),
    path('login2/',obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
