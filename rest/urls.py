from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views
from .views import *
""" 
router = routers.DefaultRouter()
router.register(r'users', UserViewSet) """

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', UserViewSet.as_view()),
    path('book', BookViewSet.as_view()),
]
