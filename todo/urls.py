from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='todo'),
    path('todo_view/<int:id>', views.todo_view, name='todo_view'),
    path('todo_edit/<int:id>', views.todo_edit, name='todo_edit'),
    path('todo_create/', views.todo_create, name='todo_create'),
    path('todo_delete/<int:id>', views.todo_delete, name='todo_delete')
]

