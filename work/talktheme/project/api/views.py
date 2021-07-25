from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def draw(request):
    from .apis.talktheme.draw import drawTalkTheme
    response = drawTalkTheme()
    return Response(response)