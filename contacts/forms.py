#add some forms.
#try to see the change connectedt to the task in github.
#checking ALM Project management trhough the pycharm and github zxzxczx

from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'

    # name = forms.CharField(
    #     label=_("Name"),
    #     max_length=255,
    # )
    #
    # email = forms.EmailField(
    #     label=_("Email address"),
    # )
    #
    # def clean_email(self):
    #
    #     if (self.cleaned_data.get('email', '')
    #         .endswith('hotmail.com')):
    #
    #         raise ValidationError("Invalid email address.")
    #
    #     return self.cleaned_data.get('email', '')