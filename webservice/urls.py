from django.conf.urls import include, url
from rest_framework import routers
from timer import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'company', views.CompanyViewSet)
router.register(r'times', views.TimeRecordViewSet)

urlpatterns = [
	url(r'^', include(router.urls))
]