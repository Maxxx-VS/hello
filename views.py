import os
import datetime
# import openpyxl
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from mysite import settings
from .forms import PhotoUploadForms, RegistrationForm
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .utils import authenticate

# def branches(request, name, sity, age):
#     return HttpResponse(f"""
#         <h1>Я живу в: {country}</h1>
#         <h1>Я живу в городе: {sity}</h1>
#         <h1>Родной язык: {age} годам</h1>

# def about(request):
#     # return render(request, "london.html")
#     # header = "Данные пользователя"
#     # langs = ["Python", "Java", "C#"]
#     # user = {"name" : "Tom", "age" : 23}
#     # adress = ("Абрикосовая", 23, 45)
#     # data = {"header": header, "langs": langs, "user":user, "adress":adress }
#     i = ["Python", "Java", "C#", "Go", "C++", "JS"]
#     # return HttpResponse('About web')) #!!!!!
#     return render(request, "london.html", context=i)

#   host = request.META["HTTP_HOST"] #адрес сервера
#   user_agent = request.META["HTTP_USER_AGENT"] #данные браузера
#   path = request.path #пути
#   return HttpResponse(f"""
#       <p>Host: {host}</p>
#       <p>Path: {path}</p>
#       <p>User-agent: {user_agent}</p>
#""")
#   return HttpResponse("Hello!", headers={"SecretCode": "123456"})
#   return HttpResponse("<h1>Hello!,<h1/>", content_type='text/plain', charset="UTF-8")
#   return HttpResponse("<h1>Hello!<h1/>", status=400, reason="Incorrect data")
#     return HttpResponse("<h1>Главная<h1/>")

# def user(request, name, sity, age):
#     return HttpResponse(f"""
#         <h1>Меня зовут: {name}</h1>
#         <h1>Я живу в городе: {sity}</h1>
#         <h1>Моя старость равна: {age} годам</h1>
# """)

# def about(request):
#     return HttpResponse('About web')

# def abo(request, name, age):
#     return HttpResponse(f"""
#         <h2>О пользователе</h2>
#         <p>Имя: {name}</p>
#         <p>Возраст: {age}</p>
# """)
#
# def con(request):
#     return HttpResponse('Con')
# def products(request):
#     return HttpResponse("Список товаров")
# def new(request):
#     return HttpResponse("Новые товары")
# def top(request):
#     return HttpResponse("Топ за неделю")

# data = ["Python", "Java", "C#", "Go", "C++", "JS"]
# return HttpResponse('About web')) #!!!!!
# class MyClass:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

menu = [
        {'title': "Новости", 'url_name': 'news'},
        {'title': "Руководство компании", 'url_name': 'management'},
        {'title': "О компании", 'url_name': 'about'},
        {'title': "Контакты", 'url_name': 'contacts'},
        # {'title': "Главная страница городов", 'url_name': 'branches'},
        # {'title': "Архив по годам", 'url_name': 'archive'},
        # {'title': "Кухня", 'url_name': 'cooking'}
]

data_db = [
    {'id': 1, 'title': 'Анкерно-угловая опора', 'content': 'Описание А-УО', 'is_published': True},
    {'id': 2, 'title': 'Промежуточная опора', 'content': 'Описание ПО', 'is_published': True},
    {'id': 3, 'title': 'Концевая опора', 'content': 'Описание КО', 'is_published': True}
]
def index_photo(request):
    return render(request, 'index_photo.html')

def upload_photo(request):
    if request.method == 'POST':
        form = PhotoUploadForms(request.POST, request.FILES)
        if form.is_valid():
            photo = form.cleaned_data['photo']
        return HttpResponseRedirect('/hello/')
    else:
        form = PhotoUploadForms()
    return render(request, 'upload.html', {form: form})
def index(request):
    data = {
        'title': "Главная страница",
        'menu': menu,
        'posts': data_db,
        # 'float': 26.58,
        # 'lst': [1, 2, "abx", True],
        # 'set': {1, 2, 3 ,5, 2},
        # 'dict': {'key_1': 'vlue_1', 'key_2': 'vlue_2'},
        # 'obj': MyClass(10, 20)
    }
    return render(request, 'index.html', context=data)
def show_more(rerequest, more_id):
    return HttpResponse(f'Отображение строки с id = {more_id}')
def news(request):
    data = {'title': "Новости"}
    return render(request, 'news.html', data)
def management(request):
    return HttpResponse("<h1>Руководство компании</h1")
def about(request):
    return render(request, 'about.html', {'title': 'О компании'})
def contacts(request):
    return HttpResponse("<h1>Контакты</h1")
def branches(request):
    return HttpResponse("Главная страница городов")
def london(request):
    sity = ["london", "paris", "moscow", "omsk", "ekb", "vladivostok"]
    data = {"s": sity}
    return render(request, "london.html", context=data)
def paris(request):
    return render(request, "paris.html")
def cooking(request):
    return render(request, "cooking.html")
def plov(request, portion):
    return HttpResponse(f"<h1>Вы готовите ПЛОВ на {portion} порций</h1>"
                        f"<li>Мясо {int(2 * portion)} кг. </li>"
                        f"<li>Рис {int(3 * portion)} кг. </li>"
                        f"<li>Морковь {int(1 * portion)} кг. </li>"
                        f"<li>Лук {int(1 * portion)} кг. </li>")
def soup(request, portion):
    return HttpResponse(f"<h1>Вы готовите СУП на {portion} порций</h1>"
                        f"<li>Картошка {int(3 * portion)} кг. </li>"
                        f"<li>Макароны {int(2 * portion)} кг. </li>"
                        f"<li>Морковь {int(4 * portion)} кг. </li>"
                        f"<li>Лук {int(6 * portion)} кг. </li>")
def porridge(request, portion):
    return HttpResponse(f"<h1>Вы готовите КАШУ на {portion} порций</h1>"
                        f"<li>Мясо {int(4 * portion)} кг. </li>"
                        f"<li>Рис {int(5 * portion)} кг. </li>"
                        f"<li>Морковь {int(3 * portion)} кг. </li>"
                        f"<li>Лук {int(2 * portion)} кг. </li>")
def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Эта страница не найдена!<br>"
                                "поищи другю страницу</h1>")
def archive(request, year):
    if year > 2023:
        return redirect('home') # перенаправление на другие URL адреса
        # url = reverse('news', args=("sport", ))
        # return HttpResponseRedirect(url)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')
@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            save_to_file(username, password)
            return render(request, 'hello/registration_success.html')
    else:
        form = RegistrationForm()
    return render(request, 'hello/register.html', {'form': form})

def save_to_file(username, password):
    file_path = settings.USER_DATA_FILE
    with open(file_path, 'a') as file:
        file.write(f"Username: {username}, Password: {password}\n")


@csrf_exempt
def biography(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user_text = form.cleaned_data['biography']
            save_to_biography(username, user_text)
            return render(request, 'hello/registration_success.html')
    else:
        form = RegistrationForm()
    return render(request, 'hello/biography.html', {'form': form})

def save_to_biography(username, biography):
    file_path = settings.USER_DATA_FILE
    # with open(file_path, 'a') as file:
    #     file.write(f"Username: {username}, Biography: {biography}\n")

    with open("biography.json", "a", encoding='utf-8') as file:
        file.write(f"Username: {username}, Biography: {biography}\n")
        # players_ststs = json.load(file)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if authenticate(username, password):
            login(request, username)
            return HttpResponseRedirect('secret_page')
    return render(request, 'hello/login.html')
@login_required
def secret_page(request):
    return render(request, 'hello/login_required.html')














