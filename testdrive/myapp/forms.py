from django import forms

CARS = ((1, 'Lada'), (2, "Audi"), (3, 'BMW'))

class UserForm(forms.Form):
    name = forms.CharField(label='Имя')
    phone = forms.IntegerField(label='Телефон')
    email = forms.EmailField(label='Почта')
    car = forms.ChoiceField(label='Марка машины',choices=CARS)
    comment = forms.CharField(label='Комментарий', widget=forms.Textarea)



