# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.shortcuts import RequestContext
from django.http import HttpResponseRedirect
#from models import MODELNAME

from django.conf import settings
import os
import csv

def homepage(request):
    data = list()

    with open('predictions.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)

    return render(request,"home.html", {"data": data})

def how_page(request):
    # Testing the scheduler with the code below (remove when done!)
    data = list()

    with open('test.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)

    return render(request, "how.html", {"data": data})

def about_page(request):
    return render(request,"about.html")
