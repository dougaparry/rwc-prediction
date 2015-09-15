#!/usr/bin/env python

# change back from predictionstest to just predictions and change the number of
# times to run the loop back to 40!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

import unirest
import csv
import boto3
import json
import yaml
import urllib2

from bs4 import BeautifulSoup

# Function to get the fixtures data from SuperSport

def getData(url):
    r = unirest.get(url)
    data = BeautifulSoup(r.raw_body,"lxml")
    cells= data.find_all("td",{"class":"cellfirst"})
    return cells

# Function to clean the fixtures data return an array of the fixtures information

def fixtures():
    url = "http://www.supersport.com/rugby/rugby-world-cup/fixtures"
    data = getData(url)

    fixtures = list()

    i = 0
    j = 1

    while i < len(data):
        if j <= 21 and data[i+1].text == "USA":
            data[i+1] = "United States"
            fixtures.append([j,data[i].text + '/09/15',data[i+5].text,data[i+1], data[i+3].text,data[i+4].text])
        elif j <= 21 and data[i+3].text == "USA":
            data[i+3] = "United States"
            fixtures.append([j,data[i].text + '/09/15',data[i+5].text,data[i+1].text, data[i+3],data[i+4].text])
        elif j <= 21 and data[i+1].text != "USA" and data[i+3].text != "USA":
            fixtures.append([j,data[i].text + '/09/15',data[i+5].text,data[i+1].text, data[i+3].text,data[i+4].text])
        elif j > 21 and data[i+1].text == "USA":
            data[i+1] = "United States"
            fixtures.append([j,data[i].text + '/09/15',data[i+5].text,data[i+1], data[i+3].text,data[i+4].text])
        elif j > 21 and data[i+3].text == "USA":
            data[i+3] = "United States"
            fixtures.append([j,data[i].text + '/09/15',data[i+5].text,data[i+1].text, data[i+3],data[i+4].text])
        elif j > 21 and data[i+1].text != "USA" and data[i+3].text != "USA":
            fixtures.append([j,data[i].text + '/09/15',data[i+5].text,data[i+1].text, data[i+3].text,data[i+4].text])

        j +=1
        i +=7

    return fixtures

#Function to receive the probabilities from the API

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

#Function to read in the values and send them to the receiveProbs Function
#Determines the winner and winning probabilities

def get_predictions():
    data = fixtures()
    new_data = list()

    for item in data:
        if int(item[0]) < 3:
            probabilities = receiveProbs(item[3], item[4])
            if probabilities[0] < probabilities[1]:
                item.append(item[3])
                item.append(round(float(probabilities[1])*100,2))
                new_data.append(item)
            else:
                item.append(item[4])
                item.append(round(float(probabilities[0])*100,2))
                new_data.append(item)

    return new_data

# function to create the predictions CSV file

def writeCSV(list):
    with open('predictionstest.csv','w') as csvfile:
        writer = csv.writer(csvfile, delimiter = ',')
        for item in list:
            writer.writerow(item)

def sign(key, msg):
    return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()

def getSignatureKey(key, dateStamp, regionName, serviceName):
    kDate = sign(("AWS4" + key).encode("utf-8"), dateStamp)
    kRegion = sign(kDate, regionName)
    kService = sign(kRegion, serviceName)
    kSigning = sign(kService, "aws4_request")
    return kSigning

# Function to upload the CSV file to the Amazon S3 Bucket

def upload():
    s3 = boto3.resource('s3')

    data = open('predictionstest.csv', 'rb')
    s3.Bucket('rwcbucket').put_object(Key='predictionstest.csv', Body=data)

def predictionsCSV():
    data = get_predictions()
    writeCSV(data)
    upload()

def main():
    predictionsCSV()

if __name__=='__main__':
    main()
