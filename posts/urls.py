from django.urls import path,include
from posts import views

app_name = "posts"


urlpatterns = [
    path('create/',views.create_post, name ="create_post"),
    path('<int:id>/delete/',views.delete_post, name ="delete_post"),
    # path('<int:id>/edit/',views.edit_task, name ="edit_task"),
    path('<int:id>/edit/',views.edit_task, name ="edit_task"),
]