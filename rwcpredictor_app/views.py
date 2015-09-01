# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.shortcuts import RequestContext
from django.http import HttpResponseRedirect
#from models import MODELNAME

from django.conf import settings

#necessary for requesting & handling data from Domino API
import unirest
import json
import yaml

import os
import csv

def receiveProbs(teamA, teamB):
    response = unirest.post("https://app.dominodatalab.com/v1/Arnu/rwcPrediction/endpoint",
        headers={
            "X-Domino-Api-Key": "iuGyjiXexOrCzjFPsNs3mkBRO2ztIvxhHBEYmtfVmiUjbaUbb4HeS5E0x8Uk3WhP",
            "Content-Type": "application/json" },
        params=json.dumps({
            "parameters": [teamA, teamB]}))

    response_data = yaml.load(response.raw_body)
    probability = response_data['result']
    return probability

def homepage(request):
    data = list()

    with open('fixtures.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)

    return render(request,"home.html", {"data": data})

def how_page(request):
    return render(request, "how.html")

def about_page(request):
    return render(request,"about.html")

def prediction(request, page_name):
    data = list()
    new_data = list()
    with open('fixtures.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)

    for item in data:
        if int(item[0]) == int(page_name):
            probabilities = receiveProbs(item[3], item[4])

            if probabilities[0] < probabilities[1]:
                winner = item[3]
                item.append(winner)
                percent = float(probabilities[1]) *100
                item.append(percent)
                new_data.append(item)
            else:
                winner = item[4]
                item.append(winner)
                percent = float(probabilities[0]) *100
                item.append(percent)
                new_data.append(item)

    return render(request, 'results.html', {'data': data, 'new_data': new_data, "gameID": page_name})
