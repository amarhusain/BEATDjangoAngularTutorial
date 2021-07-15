from django.conf.urls import url
from DepartmentApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^$', views.departmentApi),
    url(r'^([0-9]+)$', views.departmentApi)
]
