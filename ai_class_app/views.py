from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage #Si se crea directamente en FUNCIONA 1
from .file import ModelFormWithField #Si se crea desde un modelo 2
from django.views import generic #Esto para vistas por clase
from .models import Book, Author, BookInstance, Genre, Algoritmo
from .forms import UploadFileForm

def subir_archivo(request, pk):
	form = None
	if request.method == 'POST':
		form = ModelFormWithField(request.POST, request.FILES)
		print(form)
		if form.is_valid():
			form.save()
			print('Form valid')
			return render(request, 'apriori.html')
		print('Form not valid')
	else:
		form = ModelFormWithField()

	context = {'form':form}
	return render(request,'index.html', context)
	


def licencias(request):
 	return render(request,'licencias.html')

def index(request):
	return render(request,'index.html')

class AlgoritmListView(generic.ListView):
	
	model = Algoritmo
	context_object_name = 'algoritmo_list'
	template_name = 'ai_class_app/algoritmo_list.html'
#	def get_context_data(self, **kwargs):
#		# Call the base implementation first to get a context
#		context = super(AlgoritmListView, self).get_context_data(**kwargs)
#		# Get the blog from id and add it to the context
#		context['some_data'] = 'This is just some data'
#		return context
#	#queryset = Algoritmo.objects.filter(title_icontains='war')[:5] #Filtra los algoritmos que contienen la palabra war
#	def get_queryset(self):
#		return Algoritmo.objects.filter(title_icontains='war')[:5] #Filtra los algoritmos que contienen la palabra war

	

class AlgoritmDetailView(generic.DetailView):
	model = Algoritmo

	

	#context = {'form':form}
	#return render(request,'index.html', context)


# FUNCIONA 1
# def simple_upload(request):
# 	if request.method == 'POST' and request.FILES['myfile']:
# 		myfile = request.FILES['myfile'] #Nombre 'file' viene desde el html
# 		fs = FileSystemStorage()
# 		filename = fs.save(myfile.name, myfile)
# 		uploaded_file_url = fs.url(filename)
# 		return render(request, "apriori.html", {
# 			'uploaded_file_url': uploaded_file_url
# 			})
# 	return render(request, 'apriori.html')


# FUNCIONA 2
# def model_upload(request):
# 	form = None
# 	if request.method == 'POST':
# 		form = ModelFormWithField(request.POST, request.FILES)
# 		print(form)
# 		if form.is_valid():
# 			form.save()
# 			print('Form valid')
# 			return render(request, 'apriori.html')
# 		print('Form not valid')
# 	else:
# 		form = ModelFormWithField()

# 	context = {'form':form}
# 	return render(request,'index.html', context)

class BookListView(generic.ListView):
	model = Book
	context_object_name = 'my_book_list'   # your own name for the list as a template variable
	queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
	template_name = 'ai_class_app/book_list.html'  # Specify your own template name/location

class BookDetailView(generic.DetailView):
	model = Book