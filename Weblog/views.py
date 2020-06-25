from django.shortcuts import render
from .models import *
from django.http import JsonResponse

# Create your views here.

def index(request):
    authors = Author.objects.all()
    entrys = Entry.objects.all()
    return render(request, 'index.html', {'authors': authors, 'entrys': entrys})

def ajax(request):
    if request.is_ajax and request.method == 'POST':
        print(request.POST['option'])
        reportes_dic = {
            0: default,
            1: author_rating,
            2: author_comment,
        }
        opcion = int(request.POST['option'])
        funcion = reportes_dic[opcion]
        return funcion(request)
    return render(request, 'reportes/reportes.html', {})

def default(request):
    return JsonResponse(data={'response': {}}, safe=False)

def author_rating(request):
    return JsonResponse(data={'response': {}}, safe=False)

def author_comment(request):
    context = {}
    for author in Author.objects.all():
        entrys_author = author.entry_set.all()
        entrys_author = [i.number_of_comments for i in entrys_author]
        entrys_author = sum(entrys_author)
        context[author.name] = entrys_author
    return JsonResponse(data={'response': context}, safe=False)

