from django.contrib import admin

# Register your models here.
from .models import Author

admin.site.site_header = 'Custom Admin Header'  # Set the header text
admin.site.site_title = 'Custom Admin Title'    # Set the browser tab title
admin.site.index_title = 'Custom Admin Index'   # Set the home page title

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id','name','email']

admin.site.register(Author,AuthorAdmin)


