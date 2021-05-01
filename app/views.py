from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.

@api_view(['GET','POST','PUT','DELETE'])
def student_api(request,pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudetSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudetSerializer(stu,many=True)
        return Response(serializer.data)


    if request.method == 'POST':
        serializer  = StudetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'})
        return Response(serializer.errors)


    if request.method == "PUT":
        id = pk
        stu = Student.objects.get(id = id)
        serializer = StudetSerializer(stu,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complate data update'})
        return Response(serializer.errors)


    if request.method == "PATCH":
        id = pk
        stu = Student.objects.get(id = id)
        serializer = StudetSerializer(stu,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partial data update'})
        return Response(serializer.errors)


    if request.method == 'DELETE':
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'delete succesfully'})





