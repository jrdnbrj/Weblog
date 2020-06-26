from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.core import serializers

# Create your views here.

def index(request):
    authors = Author.objects.all()
    entrys = Entry.objects.all()
    return render(request, 'index.html', {'authors': authors, 'entrys': entrys})

def option(request):
    context = {}
    if request.is_ajax and request.method == 'GET':
        for author in Author.objects.all():
            entrys_author = author.entry_set.all()
            entrys_author = [i.rating for i in entrys_author]
            if request.POST['option'] == '1':
                context[author.name] = sum(entrys_author) / len(entrys_author)
            elif request.POST['option'] == '2':
                context[author.name] = sum(entrys_author)
    return JsonResponse(data={'response': context}, safe=False)

def text(request):
    context = {}
    if request.is_ajax and request.method == 'GET':
        text = request.GET['text']

        authors_name = Author.objects.filter(name__icontains=text)
        authors_email = Author.objects.filter(email__icontains=text)
        authors = authors_name.union(authors_email)

        entries_headline = Entry.objects.filter(headline__icontains=text)
        entries_body_text = Entry.objects.filter(body_text__icontains=text)
        entries_authors = Entry.objects.filter(authors__name__icontains=text)
        entries = entries_headline.union(entries_body_text, entries_authors)

        context['authors'] = serializers.serialize('json', authors)
        context['entries'] = serializers.serialize('json', entries)

    return JsonResponse(data=context, safe=False)
