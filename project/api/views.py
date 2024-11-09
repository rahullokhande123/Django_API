
# from django.shortcuts import render
# from django.http import HttpResponse,JsonResponse
# from .models import Student
# from .serializers import StudentSerializer
# from rest_framework.renderers import JSONRenderer
# import io
# from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt

# # Create your views here.

# # def student_list(req):
# #     stu = Student.objects.all() # -----------------
    
# #     serializer = StudentSerializer(stu,many=True) # -------------------
    
# #     # json_data = JSONRenderer().render(serializer.data)
# #     # print("Json_data = ",json_data)
# #     # return HttpResponse(json_data,content_type='application/json')
# #     # when we send json data from views then contet type must be a "application/json" 
# #     return JsonResponse(serializer.data,safe=False) # -----------
# #     # first argument of JsonResponse should be a dict, otherwise set safe=False

# # def student_detail(req,pk):
# #     user = Student.objects.get(pk=pk)
# #     # print(type(user))
# #     # print("Stu_name= ",user.name)
# #     # print("Stu_roll= ",user.roll)
# #     # print("Stu_city= ",user.city)
# #     serializer = StudentSerializer(user)
# #     # print("Serializer= ",serializer)
# #     # print(serializer.data)

# #     # json_data = JSONRenderer().render(serializer.data)
# #     # print("Json_data = ",json_data)
# #     # return HttpResponse(json_data,content_type='application/json')
# #     # when we send json data from views then contet type must be a "application/json" 
# #     return JsonResponse(serializer.data,safe=False)
# #     # first argument of JsonResponse should be a dict, otherwise set safe=False

# @csrf_exempt
# def stu_api(request):
#     if request.method=="GET":
#         json_data=request.body
#         print("Hello")
#         print(json_data)
#         if json_data:
#             stream = io.BytesIO(json_data)
#             python_data=JSONParser().parse(stream)
#             print(python_data)
#             id = python_data.get('id')

#             stu=Student.objects.get(id=id)
#             serializer=StudentSerializer(stu)
#             return JsonResponse(serializer.data,safe=False)

#         else:
#             stu_all=Student.objects.all()
#             serializer=StudentSerializer(stu_all,many=True)
#             return JsonResponse(serializer.data,safe=False)
        
#     elif request.method=="POST":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         serializer =StudentSerializer(data = python_data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data Created'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')
    
#     elif request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         stu = Student.objects.get(id=id)
#         # serializer = StudentSerializer(stu, data=python_data, partial = True)
#         serializer = StudentSerializer(stu, data=python_data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Data Updated !!'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')

#     elif request.method == 'PATCH':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         stu = Student.objects.get(id=id)
#         serializer = StudentSerializer(stu, data=python_data, partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Data Partially Updated...!!'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')  
 
#     elif request.method == 'DELETE':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         if id:
#             stu = Student.objects.get(id=id)
#             stu.delete()
#             res = {'msg': 'Data Deleted!!'}
#             return JsonResponse(res, safe=False)
#         else:
#             res = {'msg': 'id not present in Database'}
#             return JsonResponse(res)

        

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt       

# from api.models import Movie 
# from api.serializers import MovieSerializer 
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework import status

# @api_view(['GET', 'POST'])  
# def stu_list(request): 
#     if request.method=='GET':
#         movies = Student.objects.all() 
#         serializer=StudentSerializer(movies,many=True)
#         return Response(serializer.data) 
    
#     elif request.method=='POST':
#         serializer=StudentSerializer(data=request.data) 
#         if serializer.is_valid(): 
#             serializer.save() 
#             return Response(serializer.data) 
#         else: return Response(serializer.errors)

# @api_view(['GET', 'PUT','DELETE','PATCH']) 
# def stu_info(request,pk):
#     id = Student.objects.filter(id=pk)
#     if id:
#         if request.method=='GET': 
#             movie=Student.objects.get(id=pk) 
#             serializer = StudentSerializer(movie) 
#             return Response(serializer.data) 
        
#         elif request.method=='PUT': 
#             movie=Student.objects.get(id=pk) 
#             serializer = StudentSerializer(movie,data=request.data) 
#             if serializer.is_valid(): 
#                 serializer.save() 
#                 return Response(serializer.data) 
#             else: return Response(serializer.errors) 
        
#         elif request.method=='PATCH': 
#             movie=Student.objects.get(id=pk) 
#             serializer = StudentSerializer(movie,data=request.data,partial=True) 
#             if serializer.is_valid(): 
#                 serializer.save() 
#                 return Response(serializer.data) 
#             else: return Response(serializer.errors)
        
#         elif request.method=='DELETE': 
#                 movie=Student.objects.get(id=pk) 
#                 movie.delete() 
#                 return Response({'msg':"Data deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
#     else:
#         res = {'msg': 'id not present in Database'}
#         return Response(res)

# =================== Class Based View URL ======================
 
from rest_framework.views import APIView

class Stu_list(APIView):

    def get(self, request): 
        movies = Student.objects.all() 
        serializer=StudentSerializer(movies,many=True) 
        return Response(serializer.data)
     
    def post(self, request): 
        serializer=StudentSerializer(data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        else: return Response(serializer.errors)

class Stu_info(APIView): 
    def get(self, request,pk): 
        try: 
            movie=Student.objects.get(pk=pk) 
        except Student.DoesNotExist: 
            return Response({'msg':'Detail not found'},status=status.HTTP_404_NOT_FOUND) 
        serializer = StudentSerializer(movie) 
        return Response(serializer.data) 
    
   

        