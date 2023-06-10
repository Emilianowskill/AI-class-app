from django.conf.urls import url

from . import views


urlpatterns = [

	url(r'^$', views.index, name='index'),
	url(r'^algoritms/$', views.AlgoritmListView.as_view(), name='algoritms'),
	url(r'^algoritm/(?P<pk>\d+)$', views.AlgoritmDetailView.as_view(), name='algoritmo-detail'),
	url(r'^algoritm/(?P<pk>\d+)/archivosubido/$', views.subir_archivo, name='subir-archivo'),

	url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)/archivosubido/$', views.BookDetailView.as_view(), name='book-detail'),

	#url(r'^$', views.model_upload, name='asociacion'), # FUNCIONA 2 a admin
	#url(r'^$', views.licencias, name='licencias'),

	#url(r'^$', views.simple_upload, name='asociacion'), #FUNCIONA 1
	#url('', views.asociacion, name='asociacion'),
	#url(r'^$', views.file_upload, name='file-upload'),
]

