from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView


class StudentAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data created'})
        return Response(serializer.errors)

    def put(self, request, pk, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data updated completely'})
        return Response(serializer.errors)

    def patch(self, request, pk, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, partial=True, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data updated partially'})
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data deleted'})
