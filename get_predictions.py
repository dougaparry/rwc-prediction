#!/usr/bin/env python

import unirest
import csv
import json
import yaml

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

#Function to read in the values from the CSV and send them to the receiveProbs Function
#Determines the winner and winning probabilities

def get_predictions():
    data = list()
    new_data = list()
    with open('fixtures.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)

        for item in data:
            if int(item[0]) < 41:
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

#Function to write list elements to CSV

def writeCSV(list):
    with open('predictions.csv','w') as csvfile:
        writer = csv.writer(csvfile, delimiter = ',')
        for item in list:
            writer.writerow(item)

def main():
    data = get_predictions()
    writeCSV(data)

if __name__=='__main__':
    main()
