from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    header_style = ("background-color: green; "
                    "text-align: center;"
                    "color: white;")

    header_index = f"<header style='{header_style}'><h1>ГЛАВНАЯ СТРАНИЦА</h1></header>"


    return HttpResponse(f"{header_index}")
