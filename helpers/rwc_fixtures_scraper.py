#!/usr/bin/env python

import unirest
import csv
from bs4 import BeautifulSoup

def getData(url):
    r = unirest.get(url)
    data = BeautifulSoup(r.raw_body,"lxml")
    cells= data.find_all("td",{"class":"cellfirst"})
    return cells

def writeCSV(list):
    with open('fixtures.csv','w') as csvfile:
        writer = csv.writer(csvfile, delimiter = ',')
        for item in list:
            writer.writerow(item)

def main():
    url = "http://www.supersport.com/rugby/rugby-world-cup/fixtures"
    data = getData(url)

    fixtures = list()

    i = 0
    j = 1

    #Format: game number, day,month,year, teamA, teamB, Location

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
    writeCSV(fixtures)

if __name__=='__main__':
    main()
