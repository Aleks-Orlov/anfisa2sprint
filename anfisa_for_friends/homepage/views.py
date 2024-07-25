from django.shortcuts import render

from ice_cream.models import IceCream


def index(request):
    template = 'homepage/index.html'
    # Запишите в переменную ice_cream_list QuerySet с данными
    # которые применим в templates/homepage/index
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'price', 'description'
    ).filter(
        is_published=True,
        is_on_main=True,
        category__is_published=True
    )
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template, context)
