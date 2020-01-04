from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# from .models import User
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic
import requests
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http import JsonResponse

from django.core import serializers

import json

# from models import User
from . import models

from django.db import connection

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# first load model
chatbot = ChatBot('HelloIT',
                    storage_adapter='chatterbot.storage.SQLStorageAdapter',
                    database_uri='sqlite:///database.sqlite3')

def index(request):
    return render(request, "index.html", {"users": 1})

@api_view(['GET'])
@parser_classes((JSONParser,))
# get all data from User
def chatBotGet(request, format=None):  
    result = apiChatBot(request.query_params.get('message', None))
    suggest = apiChatBot(result)
    return Response({"result": str(result),"suggest": str(suggest)})

@api_view(['POST'])
@parser_classes((JSONParser,))
# get all data from User
def chatBotPost(request, format=None): 
    return Response({"result": str(apiChatBot(request.data['message']))})  
    
 
# *********************************************
# begin common

def apiChatBot(message):    
    result = chatbot.get_response(message) 
    return result


# convert cursor to json data
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


# execute query sql with cursor
def executeQuery(sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        data = dictfetchall(cursor)
    return data
# end common
# *********************************************
 

# *********************************************
 
# begin User
@api_view(['POST'])
@parser_classes((JSONParser,))
# get all data from User
def createDataUser(request, format=None):
    data = json.loads(json.dumps(request.data))
    obj = models.User(**data)
    obj.save()
    return Response([{"id": obj.id, "result": "ok"}])


@api_view(['POST'])
@parser_classes((JSONParser,))
# get all data from User
def readDataUser(request, format=None):
    return Response(serializers.serialize("json", models.User.objects.all()))


@api_view(['POST'])
@parser_classes((JSONParser,))
# get update data from User
def updateDataUser(request, format=None):
    data = json.loads(json.dumps(request.data))
    models.User(**data).save()
    return Response({"result": "ok"})


@api_view(['POST'])
@parser_classes((JSONParser,))
# get delete data from User
def deleteDataUser(request, format=None):
    data = json.loads(json.dumps(request.data))
    models.User(**data).delete()
    return Response({"result": "ok"})


@api_view(['POST'])
@parser_classes((JSONParser,))
# get delete data from User
def findDataUser(request, format=None):
    return Response(serializers.serialize("json", models.User.objects.filter(pk=request.data['pk'])))

# end User
# *********************************************