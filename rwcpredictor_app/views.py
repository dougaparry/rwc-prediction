# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.shortcuts import RequestContext
from django.http import HttpResponseRedirect
#from models import MODELNAME

#necessary for requesting & handling data from Domino API
import unirest
import json
import yaml

#Displayling the home page:

def recieveProbs(team1, team2):
    teamA = team1
    teamB = team2

    response = unirest.post("https://app.dominodatalab.com/v1/Arnu/rwcPrediction/endpoint",
        headers={
            "X-Domino-Api-Key": "iuGyjiXexOrCzjFPsNs3mkBRO2ztIvxhHBEYmtfVmiUjbaUbb4HeS5E0x8Uk3WhP",
            "Content-Type": "application/json" },
        params=json.dumps({
            "parameters": [teamA, teamB]})
            )

    #extract information from response:
    response_data = yaml.load(response.raw_body)
    probability = response_data['result']
    return probability

def homepage(request):
    homeTeam = 'E'
    awayTeam = 'Scotland'

    probability = recieveProbs(homeTeam, awayTeam)
    if probability[0] < probability[1]:
        winner = homeTeam
    else:
        winner = awayTeam

    return render(request, "home.html",{'winner': winner,'teamA': homeTeam, 'teamB':awayTeam})
