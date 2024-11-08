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
from .models import Image
from .forms import ImageForm
from django.shortcuts import redirect
from .models import File
from .forms import FileForm
from .models import VideoFile
from .forms import VideoForm
from .models import AudioFile
from .forms import AudioForm

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
    return render(request, "firstapp/myform.html", context)

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


# загрузка изображений
def form_up_img(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    my_text = 'Загруженные изображения'
    my_img = Image.obj_img.all()
    form = ImageForm()
    context = {'my_text': my_text, "my_img": my_img, "form": form}
    return render(request, 'firstapp/form_up_img.html', context)

# удаление изображения из БД
def delete_img(request, id):
    try:
        img = Image.obj_img.get(id=id)
        img.delete()
        return redirect('form_up_img')
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Объект не найден</h2>")


# загрузка файлов pdf
def form_up_pdf(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    my_text = 'Загруженные файлы'
    form = FileForm()
    file_obj = File.objects.all()
    context = {'my_text': my_text, "file_obj": file_obj, "form": form}
    return render(request, 'firstapp/form_up_pdf.html', context)

# удаление файлов из БД
def delete_pdf(request, id):
    try:
        pdf = File.objects.get(id=id)
        pdf.delete()
        return redirect('form_up_pdf')
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Объект не найден</h2>")


# загрузка видео файлов
def form_up_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    my_text = 'Загруженные видео файлы'
    form = VideoForm()
    file_obj = VideoFile.obj_video.all()
    context = {'my_text': my_text, "file_obj": file_obj, "form": form}
    return render(request, 'firstapp/form_up_video.html', context)

# удаление видео файлов из БД
def delete_video(request, id):
    try:
        video = VideoFile.obj_video.get(id=id)
        video.delete()
        return redirect('form_up_video')
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Объект не найден</h2>")

# загрузка аудио файлов
def form_up_audio(request):
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    my_text = 'Загруженные аудио файлы'
    form = AudioForm()
    file_obj = AudioFile.obj_audio.all()
    context = {'my_text': my_text, "file_obj": file_obj, "form": form}
    return render(request, 'firstapp/form_up_audio.html', context)

# удаление аудио файлов из БД
def delete_audio(request, id):
    try:
        audio = AudioFile.obj_audio.get(id=id)
        audio.delete()
        return redirect('form_up_audio')
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Объект не найден</h2>")



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