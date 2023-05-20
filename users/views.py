from django.shortcuts import render,reverse


from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from django.http.response import HttpResponseRedirect
from users.models import User


from users.forms import UserForm



def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if username and email and password:
            user = authenticate(request, username=username, email=email, password=password)
            if user is not None:
                auth_login(request,user)

                return HttpResponseRedirect("/")
        else:    
            context={
                "title" : "Login",
                "error" : True,
                "message" : "Invalid Username or email or password "
            }
            return render(request, "users/login.html",context=context)
    else:
        context={
            "title":"Login"    
        }   
        return render(request, "users/login.html",context=context)



def logout (request):
    auth_logout(request) 
    return HttpResponseRedirect(reverse("web:index"))
    

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)



            user = User.objects.create(
                username=instance.username,
                password=instance.password,
                email=instance.email,
                first_name=instance.first_name,
                last_name=instance.last_name,
                class_name=instance.class_name,
                division=instance.division,
            )

            user = authenticate(request, username=instance.username, email=instance.email, password=instance.password)

            return HttpResponseRedirect(reverse("web:index"))
        else:
            message = generate_form_errors(form)
            form = UserForm()
            context={
                "title" : "signup",
                "error" : True,
                "message" : message,
                "form":form,
            }    
        
            return render(request, "users/signup.html",context=context)
    else:
        form = UserForm()
        context = {
            "title": "signup",
            "form" : form,
        }
        return render(request,"users/signup.html", context=context)

    return render(request,"users/signup.html")
