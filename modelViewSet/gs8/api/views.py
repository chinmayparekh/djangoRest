from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

from rest_framework import status, viewsets


# for read only views,make use of ReadOnlyModelViewSet
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
