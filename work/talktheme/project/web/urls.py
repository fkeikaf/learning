from django.urls import include, path

from . import views

app_name = 'web'
urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.product, name='product'),
    path('product/talktheme/', views.talktheme, name="talktheme"),
]