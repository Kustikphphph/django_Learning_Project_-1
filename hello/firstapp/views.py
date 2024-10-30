from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import *
from django.template.response import TemplateResponse
from .forms import UserForm
from .models import Person
from .models import Company, Product
from .models import Student, Cours
from .models import User, Account
from django.db.models import F
# Create your views here.

def index(request):
    my_kv = ['I квартал ->', 'II квартал ->', 'III квартал->',
    'IV квартал->']
    my_month = ['Январь', 'Февраль', 'Март',
    'Апрель', 'Май', 'Июнь',
    'Июль', 'Август', 'Сентябрь',
    'Октябрь', 'Ноябрь', 'Декабрь']
    context = {'my_month': my_month, 'my_kv': my_kv}
    my_text = 'Изучаем формы Django'
    context = {'my_text': my_text}
    return render(request, "firstapp/index1.html", context)

def about(request):
    return render(request, "firstapp/about.html")
def contact(request):
    return render(request, "firstapp/contact.html")
def myform(request):
    my_form = UserForm() 
    context = {"form": my_form} 
    return render(request, "firstapp/my_form.html", context)

# alex=User.objects.create(name="Александр")
# acc=Account(login="1234", password="6565")
# alex.account=acc
# alex.account.save()
# alex.account.login="qwerty"
# alex.account.password="123456"
# alex.account.save()
# def index(request):
#     people = Person.objects.all()
#     return render(request, "index.html", {"people": people})
# сохранение данных в БД

def create(request):
    if request.method == "POST":
        klient = Person()
        klient.name = request.POST.get("name")
        klient.age = request.POST.get("age")
        klient.save()
    return HttpResponseRedirect("/")
# изменение данных в БД
def edit(request, id):
    try:
        person = Person.objects.get(id=id)
        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиент не найден</h2>")
# удаление данных из БД
def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиент не найден</h2>")


# def about(request):
#     return HttpResponse("About")
# def contact(request):
#     return HttpResponseRedirect("/about")
#help
def details(request):
    return HttpResponsePermanentRedirect("/")
def m304(request):
    return HttpResponseNotModified()
def m400(request):
    return HttpResponseBadRequest("<h2>Bad Request</h2>")
def m403(request):
    return HttpResponseForbidden ( "<h2>Forbidden</h2>")
def m404(request):
    return HttpResponseNotFound("<h2>Not Found</h2>")
def m405(request):
    return HttpResponseNotAllowed("<h2>Method is not allowed</h2>")
def m410(request):
    return HttpResponseGone("<h2>Content is no longer here</h2>")
def m500(request):
    return HttpResponseServerError("<h2>Something is wrong</h2>")