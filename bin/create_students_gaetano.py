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


with open('studenti phd fbk.csv', newline='', encoding='iso-8859-1') as f:
    reader = csv.reader(f, delimiter=';')


# Save a CSV Reader object.
#reader = csv.reader(csvfile, delimiter=';')
    k = 0
    for row in reader:
      if k > 0:
        yearmonthday = datetime.today().strftime('%Y-%m-%d')
        yearmonthday = "2016-08-23"
        daymonthyear = datetime.today().strftime('%d/%m/%Y')
        daymonthyear = "23/08/2016"
        filename1 = yearmonthday
        filename2 = row[0].encode('iso-8859-1').decode('iso-8859-1') 
        filename = filename1 + "-"+filename2    + ".md"  
        new_yaml = open(filename.lower().replace(" ","_"), 'w')
        yaml_text = ""
        yaml_text += "---\n"
        yaml_text += "layout: default \n"
        surname =  row[0].encode('iso-8859-1').decode('iso-8859-1') 
        name = row[1].encode('iso-8859-1').decode('iso-8859-1')
        yaml_text += "id: " + yearmonthday + "-" + surname.replace(" ","_") + "-" + name.replace(" ","_") + "\n"
        yaml_text += "surname: " +  surname.replace("\n","") + "\n"
        yaml_text += "name: " + name  + "\n"
        yaml_text += "university: " + row[2].encode('iso-8859-1').decode('iso-8859-1')  + "\n"
        yaml_text += "date: " + daymonthyear + "\n"
        yaml_text += "aboutme: " +  row[3].encode('iso-8859-1').decode('iso-8859-1').replace("\n","<br/>")  + "\n"
        yaml_text += "from: " + row[4].encode('iso-8859-1').decode('iso-8859-1') + "\n"
        yaml_text += "research_topic: " +  row[5].encode('iso-8859-1').decode('iso-8859-1')  + "\n"
        yaml_text += "abstract: " + row[6].encode('iso-8859-1').decode('iso-8859-1').replace("\n","<br/>")  + "\n"
        yaml_text += "advisor: "  + row[7].encode('iso-8859-1').decode('iso-8859-1')  + "\n"
        yaml_text += "keywords: " + row[8].encode('iso-8859-1').decode('iso-8859-1')  + "\n"
        website = row[9].encode('iso-8859-1').decode('iso-8859-1')
        if website.lower().find('url') == "-1":
            website = "http://" + website
        yaml_text += "website: "  +   website + "\n"
        img = row[10].encode('iso-8859-1').decode('iso-8859-1')
        if img == "":
            img = "no_picture.jpg"
        email = row[11].encode('iso-8859-1').decode('iso-8859-1')
        email = email.replace('@', '<i class="fa fa-at" aria-hidden="true"></i>') 
        yaml_text += "img: " + img + "\n"
        yaml_text += 'email: ' + email + '\n'
        yaml_text += "alt: " + name + " " + surname + "\n"
        yaml_text += "modal-id: stud" + str(k) + "\n" 
        new_yaml.write(yaml_text + "---\n")
        new_yaml.close()
      k += 1
