from django.shortcuts import render, get_object_or_404
from datetime import datetime
from pymisp import PyMISP, MISPEvent
from django.http import HttpResponse, HttpResponseRedirect
import pandas as pd
from .models import Article
from .forms import ArticleForm
from django.urls import reverse

# Create your views here.

app_name='jdr/'
def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
        <h1>Interface Eclipse phase</h1>
        <p>La mort n'est qu'une péripétie</p>
        <p>Des dangers autrement plus sérieux vous guettent</p>        
    """)

def connect_misp():
    misp_url = 'https://cyberchinois.eu'
    misp_key = 'MXeOnxoTtNIf4MlzRVeOwCS2wnErwAGluj9umGYp'
    misp = PyMISP(misp_url, misp_key)
    return misp

def MISP_list_event(requests):
    misp=connect_misp()
    r=misp.search(published=True)
    listevents=[]
    for event in r:
        listevents.append([event['Event']['id'], event['Event']['info']])
    return render(requests, app_name+'/misp.html', {'events':listevents})

def view_event(requests, id_event):
    misp=connect_misp()
    r=misp.search(eventid=id_event)
    info=r[0]['Event']['info']
    attribute=[]
    objects=[]
    for z in r[0]['Event']['Attribute']:
        attribute.append(z['value'])
    try:
        for obj in r[0]['Event']['Object']:
            for attr in obj['Attribute']:
                objects.append([attr['object_relation'], attr['value']])
    except:
        pass

    return render(requests, app_name+'/display_event.html', {'event':info,
                                                             'attributes':attribute,
                                                             'objects':objects})

def view_by_tags(requests, repors_tag):
    misp = connect_misp()
    s = misp.search(tags=repors_tag)
    info=[]
    attribute=[]
    temp = []
    final = []
    for z in s:
        info = z['Event']['info']
        for attr in z['Event']['Attribute']:
            temp.append(attr['value'])
        final.append([temp[0]])
        temp = []
    return render(requests, app_name + '/display_reports.html', {'attributes': final, 'info':info})

def liste_articles(requests):
    articles = Article.objects.all()
    return render(requests, 'jdr/liste_articles.html', {'articles': articles})

def affiche_article(requests, article_id):
    art = get_object_or_404(Article, pk=article_id)
    articles = Article.objects.all()
    return render(requests, 'jdr/affiche_article.html', {'art': art, \
                                                         'articles': articles})

def article_nouveau(request):
    validation = False
    #if request.method == 'POST':
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        validation = True
        return HttpResponseRedirect(reverse('liste_articles'))
    return render(request, 'jdr/article_nouveau.html', {'form': form, \
                                                        'validation': validation})
