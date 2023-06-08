from django.shortcuts import render
#from django.views import generic
#from .files import UploadFile
#from django.conf import settings
#from django.core.files.storage import FileSystemStorage

#from .forms import CustomerForm

def licencias(request):
 	return render(request,'licencias.html')

def index(request):
	return render(request,'index.html')

def asociacion(request):
	#form = CustomerForm()
	#context = {'form':form}
    return render(request,'apriori.html')#, context)


#def upload_file(request):
#	if request.method == 'POST' and request.FILES['file']:
#		file = request.FILES['file'] #Nombre 'file' viene desde el html
#		fs = FileSystemStorage()
#		filename = fs.save(file.name, file)
#		uploaded_file_url = fs.url(filename)
#		return render(request, "apriori.html", {
#			'uploaded_file_url': uploaded_file_url
#			})
#	return render(request, 'apriori.html')