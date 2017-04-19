#!/usr/bin/python
# -*- coding: utf-8 -*-
import unicodecsv
import requests
import cgi
from cStringIO import StringIO
from datetime import datetime
url_students ="https://docs.google.com/spreadsheets/d/1UJ8eHwcBsdKRjwc6uu2KVhNIn_FSEpLMh6xqMNQ5sUY/pub?gid=191666891&single=true&output=csv"
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
        surname =  str(row[0].encode('iso-8859-1')).replace("\n","")
        filename = yearmonthday
        filename += "-" + str(row[0].encode('iso-8859-1')).lower().replace(" ","_") + ".md"
        new_yaml = open(filename, 'w')
        yaml_text = ""
        yaml_text += "---\n"
        yaml_text += "layout: default \n"
        name = str(row[1].encode('iso-8859-1'))
        yaml_text += "id: " + yearmonthday + "-" + surname + "-" + name.replace(" ","_") + "\n"
        yaml_text += "surname: " +  surname + "\n"
        yaml_text += "name: " + name  + "\n"
        yaml_text += "university: " + str(row[2].encode('iso-8859-1'))  + "\n"
        yaml_text += "date: " + daymonthyear + "\n"
        yaml_text += "aboutme: " +  cgi.escape(str(row[3].encode('iso-8859-1'))).replace("\n","<br/>").replace(":", "&#58;")  + "\n"
        yaml_text += "from: " +  cgi.escape(str(row[4].encode('iso-8859-1')))  + "\n"
        yaml_text += "research_topic: " +  cgi.escape(str(row[5].encode('iso-8859-1')). replace(":", "&#58;"))  + "\n"
        yaml_text += "abstract: " + str(row[6].encode('iso-8859-1')).replace("\n","<br/>").replace(":", "&#58;")  + "\n"
        yaml_text += "advisor: "  + str(row[7].encode('iso-8859-1'))  + "\n"
        yaml_text += "keywords: " + str(row[8].encode('iso-8859-1'))  + "\n"
        website = ""        
        try:
            website = str(row[9].encode('iso-8859-1')).replace(":", "&#58;")
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
