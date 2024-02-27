from django.db import models
from django.contrib.auth import get_user_model
user = get_user_model()
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    bio = models.TextField()
    photo = models.ImageField(upload_to="author_photos/",null=True)
    created_by = models.ForeignKey(user,on_delete=models.CASCADE,)
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Authors"



