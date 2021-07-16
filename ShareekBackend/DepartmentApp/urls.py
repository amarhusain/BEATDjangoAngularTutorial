from django.conf.urls import url
from django.urls import path
from DepartmentApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('', views.departmentApi),
    url('([0-9]+)', views.departmentApi)
]
