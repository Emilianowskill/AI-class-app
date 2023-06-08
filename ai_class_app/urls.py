from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.asociacion, name='asociacion'),
	#url(r'^$', views.file_upload, name='file-upload'),
	url(r'^$', views.licencias, name='licencias'),
	url(r'^$', views.index, name='index'),
]