#!/usr/bin/python
# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
#from io import StringIO 
import unicodecsv
import requests
from cStringIO import StringIO
from datetime import datetime
#from builtins import str, unicode, open
url_students ="https://docs.google.com/spreadsheets/d/1UJ8eHwcBsdKRjwc6uu2KVhNIn_FSEpLMh6xqMNQ5sUY/pub?gid=2103651667&single=true&output=csv"
r = requests.get(url_students)
f = StringIO(r.text.encode('iso-8859-1'))
reader = unicodecsv.reader(f, encoding='iso-8859-1')
k = 0
for row in reader:
    if k > 0:
        yearmonthday = datetime.today().strftime('%Y-%m-%d')
        yearmonthday = "2016-08-23"
        daymonthyear = datetime.today().strftime('%d/%m/%Y')
        daymonthyear = "23/08/2016"
        filename = yearmonthday
        filename += "-" + str(row[0].encode('iso-8859-1')).lower().replace(" ","_") + ".md"
        new_yaml = open(filename, 'w')
        yaml_text = ""
        yaml_text += "---\n"
        yaml_text += "layout: default \n"
        surname =  str(row[0].encode('iso-8859-1'))
        name = str(row[1].encode('iso-8859-1'))
        yaml_text += "id: " + yearmonthday + "-" + surname.replace(" ","_") + "-" + name.replace(" ","_") + "\n"
        yaml_text += "surname: " +  surname.replace("\n","") + "\n"
        yaml_text += "name: " + name  + "\n"
        yaml_text += "university: " + str(row[2].encode('iso-8859-1'))  + "\n"
        yaml_text += "date: " + daymonthyear + "\n"
        yaml_text += "aboutme: " +  str(row[3].encode('iso-8859-1')).replace("\n","<br/>")  + "\n"
        yaml_text += "from: " +  str(row[4].encode('iso-8859-1'))  + "\n"
        yaml_text += "research_topic: " +  str(row[5].encode('iso-8859-1'))  + "\n"
        yaml_text += "abstract: " + str(row[6].encode('iso-8859-1')).replace("\n","<br/>")  + "\n"
        yaml_text += "advisor: "  + str(row[7].encode('iso-8859-1'))  + "\n"
        yaml_text += "keywords: " + str(row[8].encode('iso-8859-1'))  + "\n"
        website = ""        
        try:
            website = str(row[9].encode('iso-8859-1'))
        except:
            pass
        if website.lower().find('url') == "-1":
            website = "http://" + website
        yaml_text += "website: "  +   website + "\n"
        img = ""
        try:
            img = str(row[10].encode('iso-8859-1'))
        except:
            pass
        if img == "":
            img = "no_picture.jpg"
        email = ""
        try:
            email = str(row[11].encode('iso-8859-1'))
        except:
            pass
        email = email.replace('@', '<i class="fa fa-at" aria-hidden="true"></i>') 
        yaml_text += "img: " + img + "\n"
        yaml_text += 'email: ' + email + '\n'
        yaml_text += "alt: " + name + " " + surname + "\n"
        yaml_text += "modal-id: stud" + str(k) + "\n"
        new_yaml.write(yaml_text + "---\n")
        new_yaml.close()
    k += 1