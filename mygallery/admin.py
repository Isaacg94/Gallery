from django.contrib import admin
from .models import Editor,Category,Location,Image

admin.site.register(Editor)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Image,ImageAdmin)

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('Category','Location')