#!/usr/bin/python
# -*- coding: utf-8 -*-
import weakref
import unicodecsv
import requests
import cgi
from cStringIO import StringIO
#from builtins import str, unicode, open
url_alumni ="https://docs.google.com/spreadsheets/d/1UJ8eHwcBsdKRjwc6uu2KVhNIn_FSEpLMh6xqMNQ5sUY/pub?gid=2103651667&single=true&output=csv"
r = requests.get(url_alumni)
f = StringIO(r.text.encode('iso-8859-1'))
reader = unicodecsv.reader(f, encoding='iso-8859-1')
k = 0
for row in reader:
    if k > 0:     
        year=   str(row[5].encode('iso-8859-1'))
        date = "01-01-" + year
        name= str(row[1].encode('iso-8859-1'))
        surname= str(row[2].encode('iso-8859-1'))
        filename = date
        filename += "-" + surname.lower().replace(" ","_") +"-" + name.lower().replace(" ","_")+ ".md"  
        new_yaml = open(filename.lower().replace(" ","_"), 'w')
        yaml_text = ""
        yaml_text += "---\n"
        yaml_text += "layout: default \n"     
        yaml_text += "id: " + date + "-" + surname.replace(" ","_").replace("."," ") + "-" + name.replace(" ","_").replace("."," ") + "\n"
        name = str(row[1].encode('iso-8859-1'))
        surname =  str(row[2].encode('iso-8859-1'))
        yaml_text += "name: " + cgi.escape(name)  + "\n"
        yaml_text += "surname: " +  cgi.escape(surname.replace("\n","")) + "\n"
        yaml_text += "university: " + cgi.escape(str(row[3].encode('iso-8859-1')))  + "\n"
        yaml_text += "advisor: "  + cgi.escape(str(row[4].encode('iso-8859-1')))  + "\n"
        yaml_text += "year: " + str(row[5].encode('iso-8859-1'))  + "\n"
        yaml_text += "title: " + cgi.escape(str(row[6].encode('iso-8859-1')).replace("\n","<br/>").replace(":", "&#58;").replace("."," "))  + "\n"
        new_yaml.write(yaml_text + "---\n")
        new_yaml.close()
    k += 1
      
      

     
