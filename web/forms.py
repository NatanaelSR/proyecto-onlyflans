from django import forms
from .models import ContactForm

class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(
        label='Correo',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo@correo.com'})
    )
    customer_name = forms.CharField(
        max_length=64, 
        label='Nombre',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre completo'})
    )
    message = forms.CharField(
        label='Mensaje',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 8, 'placeholder': 'Escribe tu consulta o detalle del pedido...'})
    )

class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']
        labels = {
            'customer_email': 'Correo Electrónico',
            'customer_name': 'Nombre Completo',
            'message': 'Mensaje / Detalle del Pedido',
        }
        widgets = {
            'customer_email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ejemplo@correo.com'
            }),
            'customer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tu nombre completo'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 8,
                'placeholder': 'Detalles de tu solicitud...'
            }),
        }