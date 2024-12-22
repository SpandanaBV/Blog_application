from django.contrib import admin
from .models import postmodel, Comment
# Register your models here.

class postmodeladmin(admin.ModelAdmin):
    list_display=('title','date_created')
    
    
admin.site.register(postmodel,postmodeladmin)
admin.site.register(Comment)