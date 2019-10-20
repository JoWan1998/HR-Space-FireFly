from django.forms import ModelForm, ClearableFileInput, forms

class dataForm(forms.Form):
     file = forms.FileField(label='Selecciona el archivo a subir .csv')