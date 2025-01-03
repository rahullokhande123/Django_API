
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
# #     # return HttpResponse(json_data,content_type='application/json') ??????????

# #     # when we send json data from views then contet type must be a "application/json" 

# #     return JsonResponse(serializer.data,safe=False) # ----------- ????????

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

# ======================== Basic F() Based api =====================

# @csrf_exempt
# def stu_api(request):
#     if request.method=="GET":
#         json_data=request.body
#         print("Hello")
#         print(json_data)
#         if json_data:
#             stream = io.BytesIO(json_data) ?????????
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
#         serializer =StudentSerializer(data = python_data) ??????
#         if serializer.is_valid():
#             serializer.save()??????
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
#         # serializer = StudentSerializer(stu, data=python_data, partial = True) ??????
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


#     ================================= F() Based DRF Api ===========================

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
#         serializer=StudentSerializer(data=request.data) ?????
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
#             serializer = StudentSerializer(movie,data=request.data) ????????
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

# =================== Class Based DRF API ======================
 
from rest_framework.views import APIView

# class Stu_list(APIView):

#     def get(self, request): 
#         movies = Student.objects.all() 
#         serializer=StudentSerializer(movies,many=True) 
#         return Response(serializer.data)
     
#     def post(self, request): 
#         serializer=StudentSerializer(data=request.data) 
#         if serializer.is_valid(): 
#             serializer.save() 
#             return Response(serializer.data) 
#         else: return Response(serializer.errors)

# class Stu_info(APIView): 
#     def get(self, request,pk): 
#         try: 
#             movie=Student.objects.get(pk=pk) 
#         except Student.DoesNotExist: 
#             return Response({'msg':'Detail not found'},status=status.HTTP_404_NOT_FOUND) 
#         serializer = StudentSerializer(movie) 
#         return Response(serializer.data) 
#     def put(self,request,pk): 
#         movie=Student.objects.get(pk=pk) 
#         serializer = StudentSerializer(movie,data=request.data) 
#         if serializer.is_valid(): 
#             serializer.save() 
#             # return Response(serializer.data) 
#             return Response({'msg':"Data updated successfully"})
#         else: return Response(serializer.errors) 
#     def delete(self,request,pk): 
#         movie=Student.objects.get(pk=pk) 
#         movie.delete() 
#         return Response({'msg':"Data deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# ============================= Mixin Class Basde DRF api =============================
        
# from rest_framework import mixins
# from rest_framework import generics


# class Stu_list(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# class Stu_info(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# ========================= Genric Class Based API ==============================

# from rest_framework import generics


# class Stu_list(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# class Stu_info(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# ====================== DRF Single Root By router.py ===========================


# from rest_framework import viewsets

# class MovieViewSet(viewsets.ViewSet):
#     def list(self, request):
#         # print("List")
#         # print("Basename:", self.basename)
#         # print("Action:", self.action)
#         # print("Detail:", self.detail)
#         # print("Suffix:", self.suffix)
#         # print("Name:", self.name)
#         # print("Description:", self.description)
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)

#     def create(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def update(self,request, pk):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Complete Data Updated'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def partial_update(self,request, pk):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Partial Data Updated'})
#         return Response(serializer.errors)

#     def destroy(self,request, pk):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg':'Data Deleted'})


from rest_framework import viewsets
from .models import ComStudent
from .serializers import CompleteSerializer
from rest_framework.response import Response
from django.http import Http404
# from rest_framework.permissions import IsAuthenticated

# create a viewset
# class MovieViewSet(viewsets.ReadOnlyModelViewSet):
class MovieViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

class RDStuData(viewsets.ModelViewSet):
	queryset = ComStudent.objects.all()
	serializer_class = CompleteSerializer


class search(APIView):

    def get(self, request, pk):
        snippet = ComStudent.objects.get(id=pk)
        serializer = CompleteSerializer(snippet)
        return Response(serializer.data)