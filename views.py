import os
import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


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

def index(request):
    return HttpResponse("<h1>Главная</h1>"
                        "<h2>Строка №2</h2>"
                        "<h3>Строка №3</h3>"
                        "<p>Добро пожаловать на курс по изучению фреймворка Django с нуля.<br> Мы начнем с "
                        "самых простых вещей. <br><br>"
                        "Все, что вам потребуется – "
                        "<li>базовые знания Python. Общее представление о "
                        "<li>HTML/CSS тоже пригодится"
                        "<li>но если вы раньше не сталкивались с "
                        "версткой – ничего страшного, разберемся.</p>")
def index_en(request):
    return HttpResponse("<h1>Home</h1"
                         "<h2>Line No. 2</h2>"
                         "<h3>Line No. 3</h3>"
                         "<p>Welcome to the course on learning the Django framework from scratch.<br> We'll start with "
                         "the simplest things. <br><br>"
                         "Everything you need - "
                         "<li>Basic knowledge of Python. General understanding of "
                         "<li>HTML/CSS will come in handy too"
                         "<li>but if you haven't encountered before"
                         "layout - no big deal, we'll figure it out.</p>")
def news(request):
    return HttpResponse("<h1>Новости</h1>")
    # data = {"header": "Hi Dgango!", "message": "Добро пожаловать"}
    # return render(request, "paris.html", context=data)
def management(request):
    return HttpResponse("<h1>Руководство компании</h1")
def about_company(request):
    return HttpResponse("<h1>О компании</h1")
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












