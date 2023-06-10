from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class UploadFileForm(forms.Form):
    archivo = forms.FileField()

    def limpiar_archivo(self):
        data = self.cleaned_data['archivo']
        # Remember to always return the cleaned data.
        return data

    # def model_upload(request):
#       form = None
#       if request.method == 'POST':
#           form = ModelFormWithField(request.POST, request.FILES)
    #       print(form)
    #       if form.is_valid():
    #           form.save()
    #           print('Form valid')
    #           return render(request, 'apriori.html')
    #       print('Form not valid')
    #   else:
    #       form = ModelFormWithField()

    #   context = {'form':form}
    #   return render(request,'index.html', context)

    # FUNCIONA 1
# def simple_upload(request):
#   if request.method == 'POST' and request.FILES['myfile']:
#       myfile = request.FILES['myfile'] #Nombre 'file' viene desde el html
#       fs = FileSystemStorage()
#       filename = fs.save(myfile.name, myfile)
#       uploaded_file_url = fs.url(filename)
#       return render(request, "apriori.html", {
#           'uploaded_file_url': uploaded_file_url
#           })
#   return render(request, 'apriori.html')