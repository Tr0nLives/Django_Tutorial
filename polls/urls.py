from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('flag', views.secretPage, name='egg')
]
