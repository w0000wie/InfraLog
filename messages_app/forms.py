from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'subject', 'body']
        widgets = {
            'recipient': forms.Select(attrs={
                'style': 'width: 100%; padding: 0.5rem; border-radius: 8px; border: 1px solid #ccc;'
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Asunto del mensaje',
                'style': 'width: 100%; padding: 0.5rem; border-radius: 8px; border: 1px solid #ccc;'
            }),
            'body': forms.Textarea(attrs={
                'placeholder': 'Escribe tu mensaje...',
                'rows': 4,
                'style': 'width: 100%; padding: 0.8rem; border-radius: 8px; border: 1px solid #ccc; resize: vertical;'
            }),
        }
        labels = {
            'recipient': 'Destinatario',
            'subject': 'Asunto',
            'body': 'Mensaje',
        }

class MessageReplyForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['body']  # Solo el campo del cuerpo del mensaje
        widgets = {
            'body': forms.Textarea(attrs={
                'placeholder': 'Escribe tu mensaje aquí...',
                'rows': 4,
                'style': 'width: 100%; padding: 0.8rem; border-radius: 8px; border: 1px solid #ccc; resize: vertical;'
            }),
        }
        labels = {
            'body': '',  # esto quita el "Body:"
        }
