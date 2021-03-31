from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth import authenticate
from .models import ResourceCatagory, ResourceProduct

class ResourceProductForm(forms.ModelForm):
    class Meta:
        model = ResourceProduct
        fields = ['name', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'] = forms.ModelMultipleChoiceField(queryset=ResourceProduct.objects.all())
        self.fields['name'].widget.attrs.update({'class': 'form-control'})