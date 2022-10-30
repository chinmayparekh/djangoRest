from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

from rest_framework import status, viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, \
    DjangoModelPermissions
from customPermissions import MyPermission


# check settings.py for the default basic authentication and permissions applied
# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     # authentication_classes = [BasicAuthentication]
#     # permission_classes = [IsAuthenticated]

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [MyPermission]


# for only admins,make use of IsAdminUser
class StudentModelViewSet2(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
