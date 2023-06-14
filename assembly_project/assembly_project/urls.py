# assembly_project/urls.py
from django.contrib import admin
from django.urls import path
from assembly_app.views import execute_assembly_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('execute/', execute_assembly_view, name='execute_assembly'),
]
