# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.shortcuts import RequestContext
from django.http import HttpResponseRedirect
from django.conf import settings
import os
import csv
import urllib2

def homepage(request):
    url = 'https://s3-us-west-1.amazonaws.com/rwcbucket/predictions.csv'
    data = list()

    response = urllib2.urlopen(url)
    cr = csv.reader(response)

    for row in cr:
        data.append(row)

    return render(request,"home.html", {"data": data})

def how_page(request):
    return render(request, "how.html")

def about_page(request):
    return render(request,"about.html")
