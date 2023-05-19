import json
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


from posts.models import Task


@login_required(login_url="users/login/")
def create_post(request):
    instances = Task.objects.filter(is_delete=False)
    context = {
        "title":"task page",
        "instances":instances

    }
    return render(request,"posts/create.html", context=context)

@login_required(login_url="users/login/")
def delete_post(request,id):
    instance = get_object_or_404(Task,id=id)
    instance.is_delete = True
    instance.save()

    response_data = {
        "title" : "Sucessfully Deleted",
        "message":"Task deleted sucessfully",
        "status":"success"

    }

    return HttpResponse(json.dumps(response_data),content_type="application/json")

 
def edit_task(request, id):

    task = get_object_or_404( Task, id=id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()

            return redirect('posts/create.html')
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'posts/create.html', {'form': form})   
