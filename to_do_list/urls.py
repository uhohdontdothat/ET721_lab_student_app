from django.urls import path
from .  import views

urlpatterns = [
    path('',views.index,name='todolist'),
    path('add', views.addTodoitem, name='add'),
    path("completed/<todo_id>", views.completedTodo, name='completed'),
    path("deletecompleted", views.deletecompleted, name='deletecompleted'),
    path("deleteall", views.deleteAll, name='deleteall')
]