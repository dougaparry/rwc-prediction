#!/usr/bin/env python

import unirest
import csv
import json
import yaml


#Function to write list elements to CSV

def writeCSV(list):
    with open('test.csv','w') as csvfile:
        writer = csv.writer(csvfile, delimiter = ',')
        for item in list:
            writer.writerow(item)

def main():
    data = list()
    data.append('hey')
    data.append('hello')
    data.append('world')
    writeCSV(data)

if __name__=='__main__':
    main()
