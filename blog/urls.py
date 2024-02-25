from django.urls import path
from .views import index,author_list,create_author,edit_author,delete_author

urlpatterns = [
    path('',index),
    path('author_list/',author_list,name="author_list"),
    path('create_author/',create_author,name="create_author"),
    path('edit_author/<int:id>/',edit_author,name="edit_author"),
    path('delete_author/<int:id>/',delete_author,name="delete_author")
]