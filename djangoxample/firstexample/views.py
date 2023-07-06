from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello(request):
    string1 = "<h1>Hello World!</h1>"
    string2 = "<h2> My name is John</h2>"
    result_string = string1 + string2
    return HttpResponse(result_string)


def root(request):
    string1 = '<h1>"Изучаем django"</h1>'
    string2 = '<strong>Автор</strong>: <i>Копендаков А.Г.</i>'
    result_string = string1 + string2
    return HttpResponse(result_string)


def about(request):
    string1 = 'Имя: Иван<br/>'
    string2 = 'Отчество: Петрович<br/>'
    string3 = 'Фамилия: Иванов<br/>'
    string4 = 'телефон: 8-923-600-01-02<br/>'
    string5 = 'email: vasya@mail.ru<br/>'
    result_string = string1 + string2 + string3 + string4 + string5
    return HttpResponse(result_string)


def href(item):
    # <a href="URL">...</a>
    return f'<a href="http://127.0.0.1:8000/firstexample/item/{item["id"]}/">{item["name"]}, {item["quantity"]} штук </a><br/>'


items_list = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
]

def items(request):
    rez = "<H1>Список товара</H1>"
    for item in items_list:
        rez += href(item)
    return HttpResponse(rez)


def item(request, number):
    rez = None
    for i in range(len(items_list)):
        if number == items_list[i]["id"]:
            rez = "<H1>Карточка товара</h1>"
            rez += f'{items_list[i]["name"]}, {items_list[i]["quantity"]} штук '
    if rez is None:
        rez = "<H1>Товар не найден</H1>"
        # rez = "---"
    return HttpResponse(rez)

