from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse


# Create your views here.

# model Object - Single Student Data

def student_detail(request, pk):
    stu = Student.objects.get(id=pk)
    print(stu)  # student object
    serializer = StudentSerializer(stu)
    print(serializer)
    print(serializer.data)  # {'name': 'Ram', 'roll': 1, 'city': 'mumbai'}

    # json_data = JSONRenderer().render(serializer.data)
    # print(json_data)  # '{"name":"Ram","roll":1,"city":"mumbai"}'

    # return HttpResponse(json_data, content_type='application/json')
    # Instead of using render and returing httprespnse, we make use of jsonresponse
    return JsonResponse(serializer.data)


# Query set -All student data
def student_list(request):
    stu = Student.objects.all()
    print(stu)  # student object
    serializer = StudentSerializer(stu, many=True)
    print(serializer)
    print(serializer.data)  # {'name': 'Ram', 'roll': 1, 'city': 'mumbai'}

    # json_data = JSONRenderer().render(serializer.data)
    # print(json_data)  # '{"name":"Ram","roll":1,"city":"mumbai"}'

    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data, safe=False)  # safe =False whenever the data is not a dict
