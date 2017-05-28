from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'login/$', views.user_login, name='login'),
	url(r'register/$', views.register, name='register'),
	url(r'logout/$', views.user_logout, name='logout'),
]