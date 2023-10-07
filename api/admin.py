from django.contrib import admin
from .models import Post, Image

class ImageAdminInline(admin.TabularInline):
    model = Image

class PostAdmin(admin.ModelAdmin):
    inlines = (ImageAdminInline,)

admin.site.register(Post, PostAdmin)
# admin.site.register(Image)
# Register your models here.
