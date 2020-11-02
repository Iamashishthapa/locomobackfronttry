from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import static
from .models import Ashish
from .serializers import AshishSerializer


class Ashishview(APIView):
    def get(self,request):
        data1=Ashish.objects.all()
        serializers=AshishSerializer(data1,many=True)
        return Response(serializers.data)
