from django.urls import include, re_path, path

from django.conf import settings 
from . import views
from django.contrib.auth import views as auth_views

from Login.views import LoginClass


#from django.urls import include, path, re_path


#url HIJA 2 PASO
app_name = 'Login'

urlpatterns = [
	path('',LoginClass.as_view(),name='login'),
	

	
]
