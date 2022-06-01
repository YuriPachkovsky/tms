from django.urls import path
from demo.views import *


urlpatterns = [
    path('main/', main),
    path('posts/', posts),
    path('add/', add_post),
    path('delete/<int:id>', delete_post),
    path('edit/<int:id>', edit_post),
]

