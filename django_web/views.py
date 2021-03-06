from django.shortcuts import render
from django_web.models import ArtiInfo
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    limit = 4
    arti_info = ArtiInfo.objects[:20]
    paginator = Paginator(arti_info, limit)
    page = request.GET.get('page', 1)
    print(request)
    print(request.GET)
    loaded = paginator.page(page)
    context = {
        'ArtiInfo': loaded
    }
    return render(request, 'index.html', context)
