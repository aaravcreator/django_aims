from django.urls import path
from .views import index,author_list,create_author

urlpatterns = [
    path('',index),
    path('author_list/',author_list,name="author_list"),
    path('create_author/',create_author,name="create_author")
]