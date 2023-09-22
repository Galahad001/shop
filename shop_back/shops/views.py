from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from .serializers import TovarSerializer

@api_view(['GET'])
def API_View(request):
    if request.method == 'GET':
        tov = Tovar.objects.all()
        serializer = TovarSerializer(tov, many=True)
        return Response(serializer.data)



# Create your views here.
