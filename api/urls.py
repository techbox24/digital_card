from django.urls import path
from .views import login, login_redirect, user_details

urlpatterns = [
    path('login/', login, name='login'),
    path('login/redirect/', login_redirect, name="login_redirect"),
    path('home/', user_details, name="user_details")
]