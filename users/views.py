from django.shortcuts import render

from django.contrib.auth import authenticate, login as auth_login
from django.http.response import HttpResponseRedirect

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
    
