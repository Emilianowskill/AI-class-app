from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage #Si se crea directamente en FUNCIONA 1
from .file import ModelFormWithField #Si se crea desde un modelo 2
#from django.views import generic #Esto para vistas por clase


def licencias(request):
 	return render(request,'licencias.html')

def index(request):
	return render(request,'index.html')

#class AlgoritmListView(generic.ListView):
	# class Meta:
	# 	model = Algoritmo
	# 	fields = '__all__'
	
#	model = Algoritmo
	#context_object_name = 'lista_de_algoritmos'
	#queryset = Algoritmos.objects.filter(title_icontains='war')[:5] #Filtra los algoritmos que contienen la palabra war
	#template_name = 'Algoritms/algoritm_detail_view.html'
	
	#return render(request, 'Algoritms/algoritm_detail_view.html')

# class AlgoritmDetailView(generic.DetailView):
# 	model = Algoritmo

# 	def algoritm_detail_view(request, pk):
# 		try:
# 			algoritm_id = Algoritm.objects.get(pk=pk)
# 		except Algoritm.DoesNotExist:
# 			raise Http404("No se encontró el algoritmo")

# 		return render(
# 			request, 
# 			'algoritms/algoritm_detail_view.html'),
# 			context = {'algoritm':algoritm_id,}


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
def model_upload(request):
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
