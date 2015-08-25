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

#need to edit so that the last rows for the quarters etc dont send through to Arnu
# need to cache results and send on a timer because first try took 198 second second try took 190 seconds to
#send 48 requests - TOO LONG

    with open('fixtures.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)

    # test = list()
    # test.append(receiveProbs("New Zealand", "South Africa"))
    # test.append(receiveProbs("New Zealand", "South Africa"))
    # test.append(receiveProbs("New Zealand", "South Africa"))
    # test.append(receiveProbs("New Zealand", "South Africa"))
    # test.append(receiveProbs("New Zealand", "South Africa"))

    for item in data:
        if int(item[0]) < 5:
            probabilities = list()
            probabilities.append(receiveProbs(item[3], item[4]))

            if probabilities[0][0] < probabilities[0][1]:
                winner = item[3]
                item.append(winner)
                item.append(probabilities[0][1])
            else:
                winner = item[4]
                item.append(winner)
                item.append(probabilities[0][0])

    return render(request,"home.html", {"data": data})

def how_page(request):
    return render(request, "how.html")

def about_page(request):
    return render(request,"about.html")
