from django.shortcuts import render
from django.http import HttpResponse

from rango.models import Category


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_data = {'categories': category_list}
    return render(request, 'rango/index.html', context_data)


def about(request):
    return HttpResponse("Rango Welcomes to About Page!<br/><a href='/rango'>Index</a>")
