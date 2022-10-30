from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

from rest_framework import status, viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, \
    DjangoModelPermissions


# pip3 install httpie
# http POST http://127.0.0.1:8000/gettoken/ username="chinmay" password="123"
# hit the above url to generate a token for the username 'chinmay'


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


# for only admins,make use of IsAdminUser
class StudentModelViewSet2(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
