from django.urls import path

from . import views

urlpatterns = [
    path('', views.GetData, name='highscore_api')
]
