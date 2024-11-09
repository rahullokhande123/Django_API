
from django.urls import path
from .views import *

urlpatterns = [
    path("stu_info/<int:pk>",Stu_info.as_view(),name='stu_info'),
    path("stu_list/",Stu_list.as_view(),name='stu_list'),
    
    # path("stu_api/",stu_api,name='stu_api')
]