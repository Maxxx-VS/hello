from django.shortcuts import render
from django.http import HttpResponse

def index(request):

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
    return HttpResponse("<h1>Главная<h1/>")

def user(request, name, sity, age):
    return HttpResponse(f"""
        <h1>Меня зовут: {name}</h1>
        <h1>Я живу в городе: {sity}</h1>
        <h1>Моя старость равна: {age} годам</h1>
""")

# def about(request):
#     return HttpResponse('About web')

def about(request, name, age):
    return HttpResponse(f"""
        <h2>О пользователе</h2>
        <p>Имя: {name}</p>
        <p>Возраст: {age}</p>
""")

def contact(request):
    return HttpResponse('Contacts')


def products(request):
    return HttpResponse("Список товаров")
def new(request):
    return HttpResponse("Новые товары")
def top(request):
    return HttpResponse("Топ за неделю")