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

@api_view(['GET'])
def API_View_D(request, id):
    if request.method == 'GET':
        t = Tovar.objects.get(id=id)
        serializer = TovarSerializer(t)
        return Response(serializer.data)

# class ProductList(generics.ListAPIView)


# Create your views here.
