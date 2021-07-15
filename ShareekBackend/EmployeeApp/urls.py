from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

from EmployeeApp import views

urlpatterns=[

    url(r'^$', views.employeeApi),
    url(r'^([0-9]+)$', views.employeeApi),
    url(r'^SaveFile/$', views.SaveFile),
    url(r'^incrementCommision/$', views.increaseCommission)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
