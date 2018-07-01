# -*- coding: utf8 -*-
from bs4 import BeautifulSoup
import urllib.request

link = "http://metservice.intnet.mu/forecast-bulletin-french-mauritius.php"

content = str(urllib.request.urlopen(link).read())

soup = BeautifulSoup(content)


x=0
date=''
info=[]
newline=[2,7,12,17,22,27,32,37,42,45,46,63]
skip=[38,39]
for link in soup.find_all('p'):
    var=''
    textx=''
    #print(x, link.text,'utf8')
    if x==2:
        date=link.text
    if x<40 and x in newline:
        var='\n'    
    if (link.text).strip() != '' and x<71 and x not in skip:
        info.append(link.text+var)
    x+=1

filex =open('bulletins/'+date.replace(' ','').replace(',','_')+'.txt','w+')
#print(date)
#print(info)
for x in range(len(info)):
    filex.write(info[x].replace('\\r','').replace('\\n','')+'\n')
    
filex.close()
print('***TERMINATED***')