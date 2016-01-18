from django.shortcuts import render
from django.http import HttpResponse

from rango.models import Category
from rango.models import Page

from rango.forms import CategoryForm

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            return form.errors
    else:
        form = CategoryForm()
    return render(request, 'rango/add_category.html', {'form': form})


def category(request, category_name_slug):
    """
    Gets pages for the given category slug name.
    """
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass
    return render(request, 'rango/category.html', context_dict)


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_data = {'categories': category_list}
    return render(request, 'rango/index.html', context_data)


def about(request):
    return HttpResponse("Rango Welcomes to About Page!<br/><a href='/rango'>Index</a>")
