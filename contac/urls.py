
from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', views.index, name='contac'),
    path('<letter>s', views.index, name='contac'),
    path('view/<int:id>', views.view, name='view'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('create/', views.create, name='create'),
    path('delete/<int:id>', views.delete, name='delete')
]
