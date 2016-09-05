#!/usr/bin/python
# coding=iso-8859-1
#from __future__ import unicode_literals
import csv
#from io import StringIO
#import unicodecsv
import requests
#from StringIO import StringIO
from datetime import datetime
#from builtins import str, unicode, open
url_students ="https://docs.google.com/spreadsheets/d/1UJ8eHwcBsdKRjwc6uu2KVhNIn_FSEpLMh6xqMNQ5sUY/pub?gid=191666891&single=true&output=csv"
#r = requests.get(url_students)
#bytes_io = BytesIO(r.text.encode('iso-8859-1'))
#byte_str = bytes_io.read()
#text_obj = byte_str.decode('iso-8859-1')
#f=StringIO(text_obj) 
#reader = unicodecsv.reader(f, encoding='iso-8859-1')


with open('alumni phd fbk.csv', newline='', encoding='iso-8859-1') as f:
    reader = csv.reader(f, delimiter=';')


# Save a CSV Reader object.
#reader = csv.reader(csvfile, delimiter=';')
    k = 0
    for row in reader:
      if k > 0:
        
        date = "01-01-"
        surname =  row[2].encode('UTF-8').decode('iso-8859-1')
        year = row[5].encode('UTF-8').decode('iso-8859-1') 
        filename = date+year+"-"+surname    + ".md"  
        new_yaml = open(filename.lower().replace(" ","_"), 'w')
        yaml_text = ""
        yaml_text += "---\n"
        yaml_text += "layout: default \n"
        name = row[1].encode('UTF-8').decode('iso-8859-1')
        surname =  row[2].encode('UTF-8').decode('iso-8859-1') 
     #   yaml_text += "id: " + yearmonthday + "-" + surname.replace(" ","_") + "-" + name.replace(" ","_") + "\n"
        yaml_text += "name: " + name  + "\n"
        yaml_text += "surname: " +  surname.replace("\n","") + "\n"
        yaml_text += "university: " + row[3].encode('UTF-8').decode('iso-8859-1')  + "\n"
        yaml_text += "advisor: "  + row[4].encode('UTF-8').decode('iso-8859-1')  + "\n"
        yaml_text += "year: " + row[5].encode('UTF-8').decode('iso-8859-1')  + "\n"
        yaml_text += "title: " + row[6].encode('UTF-8').decode('iso-8859-1').replace("\n","<br/>")  + "\n"
        new_yaml.write(yaml_text + "---\n")
        new_yaml.close()
      k += 1