from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from models import Table
from xml.sax.handler import ContentHandler
from xml.sax import make_parser
from xmlparser import myContentHandler
import sys
import urllib,urllib2


# Create your views here.

@csrf_exempt
def analyze (request,recurso):

    theParser = make_parser()
    theHandler = myContentHandler()
    theParser.setContentHandler(theHandler)
    file = urllib2.urlopen( 'http://barrapunto.com/index.rss')
    theParser.parse(file)
    theHandler.htmlFile.close()

    print "Parse complete"


    if request.method == 'GET':
        index = open("index.html","r")
        html=index.read()

        try:
            record = Table.objects.get(resource=recurso)
            return HttpResponse(record.name+"<ul>"+html.decode('utf-8')+"</ul>")
        except Table.DoesNotExist:
            return HttpResponseNotFound('Page not found:')

    elif request.method == 'PUT':
        record = Table(resource= recurso,name =request.body)
        record.save()
        return HttpResponse('<h1>Actualizando.../h1>'+ request.body)

def get_all(request):
    list=Table.objects.all()
    respuesta="<h1> Recursos: </h1><ul>"
    for recurso in list:
        respuesta+="<li>"+recurso.resource+"  "+recurso.name+"</li>"
    respuesta+="</ul>"
    return HttpResponse(respuesta)
