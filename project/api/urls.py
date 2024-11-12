
from django.urls import path,include
from .routers import router


urlpatterns = [
    # path("stu_info/<int:pk>",Stu_info.as_view(),name='stu_info'),
    # path("stu_list/",Stu_list.as_view(),name='stu_list'),
    
    # path("stu_api/",stu_api,name='stu_api')
      path('',include(router.urls))

]