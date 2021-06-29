from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .apis.post import testPost

@api_view(['GET'])
def receive(request):
    response = testPost(request)
    return Response(response)