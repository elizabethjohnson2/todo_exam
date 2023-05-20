import json
from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect



from posts.models import Task,Completed


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


@login_required(login_url="users/login/")
def edit_task(request,id):
    instance = get_object_or_404(Task,id=id)
    if request.method == 'POST':
        edited_text = request.POST.get("edited-text")
        instance = Task.objects.get(id=id)
        if edited_text :
            instance.title = edited_text
            instance.save()

        
        return redirect("posts:create_post")
    context = {
        "title":"Edit Task Page",
        'todo_text': instance
        
    }
    return render(request,"posts/edit_task.html", context=context)


@login_required(login_url="users/login/")
def complete_task(request):
    instances = Completed.objects.filter(is_delete=False)
    context = {
        "title":"task page",
        "instances":instances

    }
    return render(request,"posts/create.html", context=context)
 
# def edit_task(request, id):

#     task = get_object_or_404( Task, id=id)

#     if request.method == 'POST':
#         form = TaskForm(request.POST, instance=task)

#         if form.is_valid():
#             form.save()

#             return redirect('posts/create.html')
#     else:
#         form = TaskForm(instance=task)
    
#     return render(request, 'posts/create.html', {'form': form})   
