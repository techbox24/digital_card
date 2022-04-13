from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('login/redirect/', login_redirect, name="login_redirect"),
    path('home/', user_details, name="user_details"),
    path('score/get', GetScore, name='get_score'),
    path('score/put', UpdateScore, name='Update_Score'),

]
