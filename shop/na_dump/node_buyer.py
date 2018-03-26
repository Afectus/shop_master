#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, django

projecthome = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if projecthome not in sys.path:
    sys.path.append(projecthome)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj.settings")
django.setup()



import time
import requests
import datetime
from django.utils import timezone
import re
from django.core import serializers

import random

from django.db.models import Sum, Count, Q, IntegerField
from django.db.models.functions import Cast

from node.models import *
from dj.views import *


#dumpdata node_buyer.json
data = buyer.objects.all()#[:100]
for i in data:
	i.f=i.f[:3] #первые 3 буквы фамилии
	i.phone=random.randint(9500000000, 9509999999)
	i.anketa=""
	print(i)
	
s = serializers.serialize('xml', data)
#s = re.sub('"phone": "[0-9]{1,20}"', '"phone": "9504090320"', s)

out = open("dump/node_buyer.xml", "w")
out.write(s)
out.close()



