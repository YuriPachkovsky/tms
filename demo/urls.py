from django.urls import path
from demo.views import *


urlpatterns = [
    path('posts/', PostListView.as_view()),
    path('add/', PostCreateView.as_view()),
    path('delete/<int:id>', delete_post),
    path('edit/<int:pk>', PostEditView.as_view()),
]

