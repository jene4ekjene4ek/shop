from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class FilterForm(forms.Form):
    price_from = forms.FloatField()
    price_to = forms.FloatField()

    brands = 

    def clean_price_from(self):
        if self.cleaned_data['price_from'] < 0:
            raise forms.ValidationError(
                "Price from should be positive.")
        return self.cleaned_data['price_from']


    def clean_price_to(self):
        if self.cleaned_data['price_to'] < 0:
            raise forms.ValidationError(
                "Price from should be positive.")
        return self.cleaned_data['price_to']