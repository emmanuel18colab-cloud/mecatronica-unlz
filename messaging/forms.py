from django import forms

class MensajeForm(forms.Form):
    contenido = forms.CharField(widget=forms.Textarea, label='Mensaje')
