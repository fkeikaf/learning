from django.urls import path

from . import views

app_name = 'testapi'
urlpatterns = [
    path('v1/receive/', views.receive, name='receive'),
]