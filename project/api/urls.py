
from django.urls import path,include
from .routers import router
from .import views


urlpatterns = [
    
    # ================ For f() based DRF API ===============
    # path('stu_info/', views.stu_info, name='stu_info')
    # path('stu_list/', views.stu_list, name='stu_list')

    # =============== For class,mixin ,genric based DRF API ==============
    # path("stu_info/<int:pk>",Stu_info.as_view(),name='stu_info'),
    # path("stu_list/",Stu_list.as_view(),name='stu_list'),
    
    # =============== For Single Root DRF API ===================
    # path("stu_api/",stu_api,name='stu_api')

    # =============== For Model Single Root DRF API ====================
      path('',include(router.urls)),
      
      path('search/<str:pk>', views.search, name='search')

]