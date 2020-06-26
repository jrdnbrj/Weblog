from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def option(request):
    context = {}

    for author in Author.objects.all():
        entrys_author = author.entry_set.all()
        if request.GET['option'] == '1':
            entrys_author = [i.rating for i in entrys_author]
            context[author.name] = sum(entrys_author) / len(entrys_author)
        elif request.GET['option'] == '2':
            entrys_author = [i.number_of_comments for i in entrys_author]
            context[author.name] = sum(entrys_author)

    return JsonResponse(data={'response': context}, safe=False)

def text(request):
    context = {}
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
