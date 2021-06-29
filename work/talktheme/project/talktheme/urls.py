from django.urls import path

from . import views

app_name = 'talktheme'
urlpatterns = [
    # main画面はwebアプリに記載
    path('', views.main, name='main'),
]