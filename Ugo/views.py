# -*- coding: utf-8 -*-
from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.utils import timezone
import pandas as pd
import lxml
import json
import uniout
import _uniout
from Ugo.url import *

# Create your views here.
def hello_world(request):
      return render(request,"index.html",{
      'current_time': str(timezone.localtime(timezone.now())),})

def hello_world2(request):
      return HttpResponse("Hello World!")


def hello_world3(request):

    #data = get_companies("3")

    #currency =data[0]

    #currency2= currency.ix[0:5,0:3]
    
    data = get_companies("3")

    currency =data[0]

    po = currency.values.tolist()
    
    title = ['self', 'stock-name', 'stock']
   
    #for i, line in enumerate(po):
    #     res = dict(zip(title,po[i]))
    
    #print res
    #for item in range(len(po)):
    
        #print(repr(po[item]).decode('unicode-escape'))
        
          
    res = []
    for row in po:
        temp_list = []
        for col in row:
	       data = json.dumps(col, ensure_ascii=False)
	       data = data.encode('utf8')
               # print data, type(data),
               temp_list.append(data)
        res.append(temp_list)
     
    res2 = []
    for row in res:
        res2.append(dict(zip(title, row)))

    #print res2[0]
    res3 = res2.decode('unicode-escape')
    content = {
        'title': title,
	'currency':res3,  
    }

    return render(request, 'index.html', content)




