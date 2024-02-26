from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    bio = models.TextField()
    photo = models.ImageField(upload_to="author_photos/",null=True)

    def __str__(self):
        return self.name



