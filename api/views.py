from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Talabaserializer
from .models import *

@api_view(['GET', 'POST'])
def Test(request):
    tex = Talaba.objects.all()
    serializer = Talabaserializer(tex, many=True)
    return Response({'status': 200, 'data': serializer.data})


@api_view(['GET', 'POST'])
def Testpost(request):
    data = request.data
    serializer = Talabaserializer(data=request.data)
    if not serializer.is_valid():
        return Response({'status':403,'xatolik':serializer.errors,'massage':'xatolik yuz berdi!'})
    serializer.save()

    return Response({'status': 200, 'data':serializer.data, 'massage': 'malumot qabul qilindi! '})


