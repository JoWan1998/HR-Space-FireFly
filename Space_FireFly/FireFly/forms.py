from django.forms import ModelForm, ClearableFileInput

from Space_FireFly.FireFly.models import data


class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br>  <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'


class FormEntrada(ModelForm):
    class Meta:
        model = data
        fields = ('nombre', 'file')
        widgets = {
            'file': CustomClearableFileInput
        }