from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    Olu = {
        "slackUsername": "olusameze", "backend": True, "age": 22, "bio": "Backend enthusiast"
    }
    return Response(Olu)
# Create your views here.
