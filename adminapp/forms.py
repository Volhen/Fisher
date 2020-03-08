from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from django.db import models
# from django.conf import settings
from django.core.files.images import get_image_dimensions

from authapp.models import FishUser
from mainapp.models import ProductCategory, Product


class FishUserCreationAdminForm(UserCreationForm):
    class Meta:
        model = FishUser
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'email', 'age', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")
        return data


class FishUserUpdateAdminForm(UserChangeForm):
    class Meta:
        model = FishUser
        # fields = '__all__'
        fields = ('username', 'first_name', 'last_name', 'email',
                  'age', 'avatar', 'password', 'is_superuser', 'is_active')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")
        return data


class ProductCategoryEditForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            # field.help_text = ''


class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
    def clean_image(self):
        data = self.cleaned_data['image']

        if data:
           w, h = get_image_dimensions(data)
           if w != h:
               raise forms.ValidationError(f'Разрешение изображения должно быть с равными сторонами (например 500x500px), а ваше имеет разрешение ({w}x{h})!!!')
        
        return data
