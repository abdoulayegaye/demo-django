from django.http import HttpResponse
from django.shortcuts import render

from .db_articles import articles

def articles_view(request):
    # return HttpResponse('Contactez-nous !')
    return render(request, 'articles/liste.html', context={'articles': articles})
