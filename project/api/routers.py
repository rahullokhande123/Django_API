from rest_framework import routers
from .views import MovieViewSet
from .views import RDStuData

router=routers.DefaultRouter()
router.register(r'movie',MovieViewSet,basename='movie')
router.register(r'',RDStuData)

urlpatterns=router.urls 