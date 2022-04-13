from django.urls import path

from . import views

urlpatterns = [
    path('get', views.GetData, name='get'),
    path('put', views.UpdateScore, name='update')
]
