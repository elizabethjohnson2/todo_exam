from django.contrib import admin

from posts.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]

admin.site.register(Task,TaskAdmin)

# class CompletedAdmin(admin.ModelAdmin):
#     list_display = ["id", "title"]

# admin.site.register(Completed,CompletedAdmin)


