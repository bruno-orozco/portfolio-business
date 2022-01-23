from django import forms
from inbox.models import *

class formMessage(forms.ModelForm):
    """ Form configuration """

    contact_full_name = models.CharField(max_length=255)

    number_phone = models.PositiveBigIntegerField()

    email = models.EmailField()

    message = models.TextField()

    class Meta:
            """ Form configuration """
            
            model = message
            fields = '__all__'
            labels = {
                "contact_full_name": "Your full name",
                "phone_number": "Your phone number",
            }
            widgets = {
                'phone_number' : forms.NumberInput(attrs={'type' : 'tel'}),
                'email' : forms.EmailInput(attrs={'placeholder' : 'optional'}),
                }

    def clean_email(self):
        """ This function is used to accept null values. """

        email = self.cleaned_data['email'] or None
        return email
