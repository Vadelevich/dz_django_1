from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super().clean()
        zag = cleaned_data.get("name_product")
        text = cleaned_data.get("title")
        if zag and text:
            if ('казино' or 'криптовалюта'or 'крипта' or 'биржа' or 'дешево' or 'бесплатно'or 'обман'or 'полиция'or 'радар') in (zag or text) :
                raise forms.ValidationError('Описание не должно содержать запрещенных слов')
        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'