from django import forms

# class UserForm(forms.Form):
#     name = forms.CharField(label="Имя клиента",
#     widget=forms.TextInput(attrs={"class": "myfield"}))
#     age = forms.IntegerField(label="Возраст клиента",
#     widget=forms.NumberInput(attrs={"class": "myfield"}))
class UserForm(forms.Form):
     file_path = forms.FilePathField(label="Выберите файл",
                                    path='C:/Users/Student28/Desktop/Урок/')
