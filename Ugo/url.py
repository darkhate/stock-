#!/usr/bin/python 
# -*- coding: utf-8 -*-
import pandas as pd
import lxml
import json
import uniout
import unicodedata
def get_companies(se = "1"):
    template = "http://www.tse.com.tw/zh/listed/listingProfileInquiry?mobile=&selectItem=3&selectSubitem={}"
    url = template.format(se)
    #print url[0]
    #print pd.read_html(url)
    return pd.read_html(url)


data = get_companies("3")

#print data[0]

currency =data[0]

#print currency

#currency2= currency.ix[0:5,0:3]

po = currency.values.tolist()

title = ['self', 'stock-name', 'stock']

'''
po2=[]
d=[]                                                          
for i in range(len(po)):                               
    new = []                       
    for j in range(len(po[i])):             
        new.append('')       
    po2.append(new)
    d.append(new)
'''
res = []
for row in po:
    temp_list = []
    for col in row:
	data = json.dumps(col, ensure_ascii=False)
	data = data.encode('utf8')
        # print data, type(data),
        temp_list.append(data)
    res.append(temp_list)

#print res

res2 = []
for row in res:
    res2.append(dict(zip(title, row)))

# print res2
title2=['stock', 'stock-name', 'self']
#print title2
#print "--------------------------------------------------------------"
for row in res2:
    i=0
    for k, v in row.items():
        if i<=3:
            print v,
    #print "     "
    #print
  
#print res2

'''
for i in range(len(po)):
   for j in range(len(po[i])):
     po[i][j]=json.dumps(po[i][j], ensure_ascii=False, encoding="utf-8")
     po[i][j]=po[i][j].encode('utf8')
     #print po2
     #print type(po2)
     if po2=='unicode':
         print "123"
         po[i][j]=(po[i][j]).encode('ascii','ignore')
         res.append(po[i][j])
         print type(res[j])


for i in range(len(po2)):
   for j in range(len(po2[i])):
       #print po2[i][j]
       d.append(zip(title,po2[i][j]))
       print d[i][j]

 
#print po[0][1]
#print type(po)
'''

'''
res = []
for i, line in enumerate(po):
    res.append(dict(zip(title, po[i])))

print res
'''
'''
po2 = json.dumps(res).decode("unicode-escape")

po3 = po2.encode('utf8')
print po3
res = []
for i, line in enumerate(po):
    res.append(dict(zip(title, po[i])))

print res
'''
#for item in range(len(po)):
#    print(json.dumps(po[item]).decode("unicode-escape"))

#    if item>=5:
#       break


