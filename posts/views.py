from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="users/login/")
def create_post(request):
    context = {
        "title":"task page"
    }
    return render(request,"posts/create.html", context=context)