import django_filters.rest_framework
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets, filters
from rest_framework.response import Response
from .serializers import *
from .models import Book



# ViewSets define the view behavior.
class UserViewSet(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['username','email']
    search_fields = ['username','email']
    ordering_fields = ['username', 'email']

    permission_classes = [IsAdminUser]


class BookViewSet(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UserViewSet1(APIView):
    def get (self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        if request.COOKIES.get('seen'):
            return HttpResponse("you have seen this message")
        res = Response(serializer.data)
        res.set_cookie('seen', True)
        return res
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ExmViewSet(APIView):
    def post(self, request):
        name = request.data.get('name')
        return HttpResponse(f'<h1>Hello {name}</h1>')

""" class UserViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAdminUser]

    queryset = User.objects.all()
    serializer_class = UserSerializer """

    