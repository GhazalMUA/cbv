from django import forms
from .models import Kelas

class KelasForm(forms.ModelForm):
    
    class Meta:
        model=Kelas
        fields='__all__'
    
    # def clean_name(self):
    #     name=self.cleaned_data.get('name')
    #     if Kelas.objects.filter(name='name').exists():
    #         raise NameError('you should enter a unique name')
    #     return name
        
    # def clean_price(self):
    #     price= self.cleaned_data.get('price')
    #     if price <= 0 :
    #         raise ValueError('price cannot be zero.')
    #     return price
        