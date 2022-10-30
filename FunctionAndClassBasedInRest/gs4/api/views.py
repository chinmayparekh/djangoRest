from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status

# Create your views here.
# @api_view(['GET'])
# def hello_world(request):
#     return Response({'msg': 'Hello World'})
#
#
# @api_view(['POST'])
# def hello_world(request):
#     if request.method == 'POST':
#         print(request.data)
#         return Response({'msg': 'This is a post request'})

#
# @api_view(['GET', 'POST'])
# def hello_world(request):
#     if request.method == 'GET':
#         return Response({'msg': 'Hello World'})
#     if request.method == 'POST':
#         print(request.data)
#         return Response({'msg': 'This is a post request'})

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_api(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, partial=True, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data updated partially'})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data deleted'})


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def student_api_with_pk(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data created'})
        return Response(serializer.errors)

    if request.method == 'PUT':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data updated completely'})
        return Response(serializer.errors)

    if request.method == 'PATCH':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, partial=True, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data updated partially'})
        return Response(serializer.errors)
    if request.method == 'DELETE':
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data deleted'})
