from django.contrib import admin

from posts.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ["id","title","delete_image","edit_image"]

admin.site.register(Task,TaskAdmin)




