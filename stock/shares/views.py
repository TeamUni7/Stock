from django.shortcuts import render
from django.template import loader
import json
from django.core import serializers
from django.conf import settings as djangoSettings
from django.http import HttpResponse
from django.http import JsonResponse

def index(request):
    template = loader.get_template("shares/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def index1(request):
    template = loader.get_template("shares/index1.html")
    context = {}
    return HttpResponse(template.render(context, request))


def update(request):
    if request.method == "POST":
        str1 = request.POST
        str1 = str1.dict()
        if 'csrfmiddlewaretoken' in str1:
            del str1['csrfmiddlewaretoken']
        x = ""
        y = ""
        temp = {}
        list1 = []
        for k, v in str1.items():
            print("Key is " + k + " Value is " + v)
            if (x == ""):
                temp = {}
                x = v
            else:
                y = v
                temp = {
                    "x": x,
                    "y": y
                }
                x = ""
                y = ""
                list1.append(temp)
        json1 = json.dumps(list1)
        '''path = '.'
        fileName = "users.json"
        filePath = path + "/" + fileName + ".json"
        with open(filePath, "w") as fp:
            json.dump(json1, fp)'''
        name = "users"
        file = open(djangoSettings.STATIC_ROOT + '\\shares\\' + name + '.json', 'w')
        file.write(json1)
        file.close()
        return JsonResponse(list1, safe = False)

def update1(request):
    if request.method == "POST": # Checking type of request (POST or GET)
        str1 = request.POST # Storing content of request.
        str1 = str1.dict() # Converting that string to python dictionary.
        #str2 = str1
        #str2 = str(str2)
        if 'csrfmiddlewaretoken' in str1:
            del str1['csrfmiddlewaretoken'] # removing csrf token from dictionary as it not a part of out data.
        Date = "" # Date part of data
        SENSEX = "" # SENSEX part of data
        NIFTY  = "" # NIFTY part of data
        NASDAQ = "" # NASDAQ part of data
        GOLD = "" # GOLD part of data
        temp = {}
        list1 = [] # List containg out data objects.
        for k, v in str1.items(): # Iterating dictionary of data
            #print("Key is " + k + " Value is " + v)
            if (Date == ""): # Storing Date Part
                temp = {} # Initialise temp
                Date = v
            elif (SENSEX == ""): # Storing SENSEX Part
                SENSEX = v
            elif (NIFTY == ""): # Storing NIFTY Part
                NIFTY = v
            elif (NASDAQ == ""): # Storing NASDAQ Part
                NASDAQ = v
            else: # Storing GOLD Part
                GOLD = v
                temp = { # Create temp
                    "Date": Date,
                    "SENSEX": SENSEX,
                    "NIFTY": NIFTY,
                    "NASDAQ": NASDAQ,
                    "GOLD": GOLD
                }
                Date = ""
                SENSEX = ""
                NIFTY = ""
                NASDAQ = ""
                GOLD = ""
                list1.append(temp) # Push it to list
                temp = {}
        json1 = json.dumps(list1) # converts python list to json formatted string
        name = "jsonData1" # name of file in whicj to be written
        file = open(djangoSettings.STATIC_ROOT + '\\shares\\' + name + '.json', 'w') # open desired file.
        file.write(json1) # write
        file.close() # close file
        #return JsonResponse(list1, safe=False)
