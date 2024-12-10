from django.urls import path,include

from rest_framework.routers import DefaultRouter
from .views import EmployeViewSet
from .views import StagiairesViewSet,PostViewSet

router = DefaultRouter()
router.register(r'employes', EmployeViewSet)
router.register(r'stagiaires', StagiairesViewSet)
router.register(r'posts', PostViewSet)
urlpatterns = [

    path('', include(router.urls)),
   
]