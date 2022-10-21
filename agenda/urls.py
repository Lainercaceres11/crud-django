
from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contac/', include('contac.urls')),
    path('todo/', include('todo.urls')),
    path('', views.index, name='index'),
]
