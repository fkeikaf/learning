from django.urls import include, path

from . import views

app_name = 'talktheme'
urlpatterns = [
    # main画面はwebアプリに記載
    path('', views.showPages, name='main'),
    path('draw/', views.showPages, name='draw'),
]