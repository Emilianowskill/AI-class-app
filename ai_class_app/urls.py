from django.conf.urls import url

from . import views


urlpatterns = [

	#url(r'^$', views.index, name='index'),
	#url(r'^algoritms/$', views.AlgoritmListView.as_view(), name='algoritmos'),
	#url(r'^Algoritms/(?<pk>\d+)$', views.AlgoritmDetailView.as_view(), name='Algoritmos-especifico'),
	url(r'^$', views.model_upload, name='asociacion'), # FUNCIONA 2 a admin
	#url(r'^$', views.licencias, name='licencias'),

	#url(r'^$', views.simple_upload, name='asociacion'), #FUNCIONA 1
	#url('', views.asociacion, name='asociacion'),
	#url(r'^$', views.file_upload, name='file-upload'),
]