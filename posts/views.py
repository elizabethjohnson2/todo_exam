from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from posts.models import Task


@login_required(login_url="users/login/")
def create_post(request):
    instances = Task.objects.filter()
    context = {
        "title":"task page",
        "instances":instances

    }
    return render(request,"posts/create.html", context=context)