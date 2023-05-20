from django.contrib import admin

from posts.models import Task,Completed

class TaskAdmin(admin.ModelAdmin):
    list_display = ["id","title","delete_image","edit_image"]

admin.site.register(Task,TaskAdmin)

class CompletedAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]

admin.site.register(Completed,CompletedAdmin)


