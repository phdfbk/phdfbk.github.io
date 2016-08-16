# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
#from io import StringIO 
import unicodecsv
import requests
from cStringIO import StringIO
from datetime import datetime
#from builtins import str, unicode, open
url_students ="https://docs.google.com/spreadsheets/d/1UJ8eHwcBsdKRjwc6uu2KVhNIn_FSEpLMh6xqMNQ5sUY/pub?gid=191666891&single=true&output=csv"
r = requests.get(url_students)
f = StringIO(r.text.encode('iso-8859-1'))
reader = unicodecsv.reader(f, encoding='iso-8859-1')
k = 0
for row in reader:
    if k > 0:
        filename = datetime.today().strftime('%Y-%m-%d')
        filename += "-" + str(row[0].encode('iso-8859-1')).lower().replace(" ","_") + ".md"
        new_yaml = open(filename, 'w')
        yaml_text = ""
        yaml_text += "---\n"
        yaml_text += "layout: default \n"
        surname =  str(row[0].encode('iso-8859-1'))
        name = str(row[1].encode('iso-8859-1'))
        yaml_text += "id: " + datetime.today().strftime('%Y-%m-%d') + "-" + surname.replace(" ","_") + "-" + name.replace(" ","_") + "\n"
        yaml_text += "surname: " +  surname + "\n"
        yaml_text += "name: " + surname  + "\n"
        yaml_text += "university: " + str(row[2].encode('iso-8859-1'))  + "\n"
        yaml_text += "date: " + datetime.today().strftime('%d/%m/%Y')  + "\n"
        yaml_text += "aboutme: " +  str(row[3].encode('iso-8859-1'))  + "\n"
        yaml_text += "from: " +  str(row[4].encode('iso-8859-1'))  + "\n"
        yaml_text += "research_topic: " +  str(row[5].encode('iso-8859-1'))  + "\n"
        yaml_text += "subtitle: " + str(row[6].encode('iso-8859-1'))  + "\n"
        yaml_text += "advisor: "  + str(row[7].encode('iso-8859-1'))  + "\n"
        yaml_text += "keywords: " + str(row[8].encode('iso-8859-1'))  + "\n"
        website = str(row[9].encode('iso-8859-1'))
        if website.lower().find('url') == "-1":
            website = "http://" + website
        yaml_text += "website: "  +   website + "\n"
        img = str(row[10].encode('iso-8859-1'))
        if img == "":
            img = "no_picture.jpg"
        yaml_text += "img: " + img + "\n"
        yaml_text += "thumbnail: " + img.replace('.jpg','') + "_thumb.jpg\n"
        yaml_text += "alt: " + name + " " + surname + "\n"
        yaml_text += "modal-id: stud" + str(k) + "\n"
        new_yaml.write(yaml_text + "---\n")
        new_yaml.close()
    k += 1