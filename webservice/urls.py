from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from timer import views

urlpatterns = [
	url(r'^$', views.UserView.as_view()),
	url(r'^user/$', views.UserView.as_view()),
	url(r'^register/$', views.RegisterView.as_view()),
	url(r'^timer/$', views.TimerView.as_view()),
	url(r'^stats/$', views.UserStatsView.as_view()),
	url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
	url(r'^api-token-refresh/', 'rest_framework_jwt.views.refresh_jwt_token'),
]

urlpatterns = format_suffix_patterns(urlpatterns)