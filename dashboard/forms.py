from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ['name', 'category', 'quantity']


# class UserUpdateForm(forms.ModelForm):
#     class Meta:
#         model = User
#         # fields = '__all__'
#         fields = ['username', 'email']
#
#
# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         # fields = '__all__'
#         fields = ['address', 'phone', 'image']
