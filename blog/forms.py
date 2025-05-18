from django import forms

from blog.models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your Name'
                    }),
            'birth_date': forms.DateInput(attrs={
                    'type': 'date',
                    'class': 'form-control',
                    }),
            'email': forms.EmailInput(attrs={
                    'class': 'form-control'
                    }),
            'subject': forms.TextInput(attrs={
                    'class': 'form-control'
                    }),
            'message': forms.Textarea(attrs={
                'class': 'form-control'
                    }),
        }
