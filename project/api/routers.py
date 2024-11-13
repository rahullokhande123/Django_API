from rest_framework import routers
from .views import MovieViewSet
from .views import RDStuData

router=routers.DefaultRouter()
router.register(r'movie',MovieViewSet,basename='movie')

urlpatterns=router.urls 