from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^apiv1/', include('timer.urls')),
    url(r'^admin/', include(admin.site.urls)),
]