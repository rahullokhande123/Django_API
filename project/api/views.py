
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer

# Create your views here.

# def student_list(req):
#     stu = Student.objects.all() # -----------------
    
#     serializer = StudentSerializer(stu,many=True) # -------------------
    
#     # json_data = JSONRenderer().render(serializer.data)
#     # print("Json_data = ",json_data)
#     # return HttpResponse(json_data,content_type='application/json')
#     # when we send json data from views then contet type must be a "application/json" 
#     return JsonResponse(serializer.data,safe=False) # -----------
#     # first argument of JsonResponse should be a dict, otherwise set safe=False

# def student_detail(req,pk):
#     user = Student.objects.get(pk=pk)
#     # print(type(user))
#     # print("Stu_name= ",user.name)
#     # print("Stu_roll= ",user.roll)
#     # print("Stu_city= ",user.city)
#     serializer = StudentSerializer(user)
#     # print("Serializer= ",serializer)
#     # print(serializer.data)

#     # json_data = JSONRenderer().render(serializer.data)
#     # print("Json_data = ",json_data)
#     # return HttpResponse(json_data,content_type='application/json')
#     # when we send json data from views then contet type must be a "application/json" 
#     return JsonResponse(serializer.data,safe=False)
#     # first argument of JsonResponse should be a dict, otherwise set safe=False


def stu_api(request):
    if request.method=="GET":
        json_data=request.body
        print(json_data)
        if json_data:
            stream = io.BytesIO(json_data)
            python_data=JSONPersar().parse(stream)
            id = python_data.get('id')
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return JsonResponse(serializer.data,safe=False)

        else:
            stu_all=Student.objects.all()
            serializer=StudentSerializer(stu_all,many=True)
            return JsonResponse(serializer.data,safe=False)

        