from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from .models import country
from.serializers import ItemSerialzer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET'])
def index(request):
    coun = country.objects.all()
    serialzer = ItemSerialzer(coun, many=True)
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    return Response(serialzer.data)

@api_view(['POST'])
def add_item(request):
    serializer = ItemSerialzer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)