from django.shortcuts import render
from .forms import UserForm, CARS
from django.http import HttpResponse

users = [
    {'name': 'Golovnya',
     'phone': '8(983)324-33-33',
     'email': 'marina@mail.ru', 'car': 'BMW'},
    {'name': 'Skripicyna',
     'phone': '8(983)324-03-33',
     'email': 'alena@mail.ru', 'car': 'BMW2'},
    {'name': 'Klyap',
     'phone': '8(983)324-33-73',
     'email': 'vladik@mail.ru', 'car': 'BMW3'}
]


def index(request):
    return render(request, "index.html", context={'users': users})


def about(request):
    return render(request, "about.html")


def record(request):
    if request.method=="POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data['name']
            phone = userform.cleaned_data['phone']
            email = userform.cleaned_data['email']
            car = int(userform.cleaned_data['car'])
            comment = userform.cleaned_data['comment']
            car = list(filter(lambda elem: elem[0] == car, CARS))[0][1]
            users.append({'name':name,
                          'phone':phone,
                          'email':email,
                          'car':car})
        else:
            return HttpResponse('Invalid data')

    userform = UserForm()
    return render(request, 'record.html', {'form':userform})
