from django.forms import ModelForm
from .models import Files
#from .models import Algoritmo

class ModelFormWithField(ModelForm):
	class Meta:
		model = Files
		fields = '__all__'

#class Algoritm(ModelForm):
#	class Meta:
#		model = Algoritmo
#		fields = '__all__'