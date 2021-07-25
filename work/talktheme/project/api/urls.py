from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('v1/talktheme/draw/', views.draw, name='draw'),
]