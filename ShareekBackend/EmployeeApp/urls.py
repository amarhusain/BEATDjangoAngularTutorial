from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.urls import path

from EmployeeApp import views

urlpatterns=[

    path('', views.employeeApi),
    path('([0-9]+)', views.employeeApi),
    path('SaveFile/', views.SaveFile),
    path('incrementCommision/', views.increaseCommission)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
