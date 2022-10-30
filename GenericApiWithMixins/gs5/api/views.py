from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin


# List and Create Mixins dont require pk
class StudentListCreate(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# Retrieve,update and destroy mixins can be grouped together as they require pk
class StudentUpdateRetrieveDelete(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update \
            (request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# List and Create Mixins dont require pk
# class StudentList(GenericAPIView, ListModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#
# class StudentCreate(GenericAPIView, CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class StudentRetrieve(GenericAPIView, RetrieveModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#
# class StudentUpdate(GenericAPIView, UpdateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def put(self, request, *args, **kwargs):
#         return self.update \
#             (request, *args, **kwargs)
#
#
# class StudentDestroy(GenericAPIView, DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
