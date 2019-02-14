# RUN THE CODE TO SEE THE OUTPUT IN THE CONSOLE!!!
import operator

import requests

# api-endpoint
URL = "https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=f599955a7a5550a3a40f9daf3029"

# sending get request and saving the response as response object
r = requests.get(url=URL, params=PARAMS)

# extracting data in json format
data = r.json()

countries = dict()
noOfPartneres = len(data['partners'])
for i in range(noOfPartneres):
    noOfDates = len(data['partners'][i]['availableDates'])
    for j in range(noOfDates):
        tempDate = data['partners'][i]['availableDates'][j].split("-")
        date = int(tempDate[1] + tempDate[2])

        if data['partners'][i]['country'] in countries:
            countries[data['partners'][i]['country']].append(date)
        else:
            countries[data['partners'][i]['country']] = [date]

for i in range(len(countries)):
    print("Country: " + str(list(countries.keys())[i]))
    numOfRecords = len(countries[data['partners'][i]['country']])
    temp = countries[data['partners'][i]['country']]
    counterMax = 0
    maxDates = dict()
    for j in range(len(temp) - 1):
        if temp[j + 1] - temp[j] == 1:
            if temp[j] in maxDates:
                maxDates[temp[j]] = maxDates[temp[j]] + 1
            else:
                maxDates[temp[j]] = 1
        else:
            continue

    if maxDates == {}:
        print("StartDate: null")
        print("Attendee Count: 0")
        print()
        continue
    sorted_d = sorted(maxDates.items(), key=operator.itemgetter(0))
    final_date = "2017-0" + str(sorted_d[0][0])[-3] + "-" + str(sorted_d[0][0])[-2:]
    print("StartDate: " + str(final_date))
    print("Attendee Count: " + str(sorted_d[0][1]))
    print()
    # print(min(maxDates, key=maxDates.get))
