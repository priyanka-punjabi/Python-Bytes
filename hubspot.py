# api-endpoint
URL = "https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=f599955a7a5550a3a40f9daf3029"

# location given here
location = "delhi technological university"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'address': location}

# sending get request and saving the response as response object
# r = requests.get(url=URL, params=PARAMS)

r = {
    "partners": [
        {
            "firstName": "Darin",
            "lastName": "Daignault",
            "email": "ddaignault@hubspotpartners.com",
            "country": "United States",
            "availableDates": [
                "2017-05-03",
                "2017-05-06"
            ]
        },
        {
            "firstName": "Crystal",
            "lastName": "Brenna",
            "email": "cbrenna@hubspotpartners.com",
            "country": "Ireland",
            "availableDates": [
                "2017-04-27",
                "2017-04-29",
                "2017-04-30"
            ]
        },
        {
            "firstName": "Janyce",
            "lastName": "Gustison",
            "email": "jgustison@hubspotpartners.com",
            "country": "Spain",
            "availableDates": [
                "2017-04-29",
                "2017-04-30",
                "2017-05-01"
            ]
        },
        {
            "firstName": "Tifany",
            "lastName": "Mozie",
            "email": "tmozie@hubspotpartners.com",
            "country": "Spain",
            "availableDates": [
                "2017-04-28",
                "2017-04-29",
                "2017-05-01",
                "2017-05-04"
            ]
        },
        {
            "firstName": "Temple",
            "lastName": "Affelt",
            "email": "taffelt@hubspotpartners.com",
            "country": "Spain",
            "availableDates": [
                "2017-04-28",
                "2017-04-29",
                "2017-05-02",
                "2017-05-04"
            ]
        },
        {
            "firstName": "Robyn",
            "lastName": "Yarwood",
            "email": "ryarwood@hubspotpartners.com",
            "country": "Spain",
            "availableDates": [
                "2017-04-29",
                "2017-04-30",
                "2017-05-02",
                "2017-05-03"
            ]
        },
        {
            "firstName": "Shirlene",
            "lastName": "Filipponi",
            "email": "sfilipponi@hubspotpartners.com",
            "country": "Spain",
            "availableDates": [
                "2017-04-30",
                "2017-05-01"
            ]
        },
        {
            "firstName": "Oliver",
            "lastName": "Majica",
            "email": "omajica@hubspotpartners.com",
            "country": "Spain",
            "availableDates": [
                "2017-04-28",
                "2017-04-29",
                "2017-05-01",
                "2017-05-03"
            ]
        },
        {
            "firstName": "Wilber",
            "lastName": "Zartman",
            "email": "wzartman@hubspotpartners.com",
            "country": "Spain",
            "availableDates": [
                "2017-04-29",
                "2017-04-30",
                "2017-05-02",
                "2017-05-03"
            ]
        },
        {
            "firstName": "Eugena",
            "lastName": "Auther",
            "email": "eauther@hubspotpartners.com",
            "country": "United States",
            "availableDates": [
                "2017-05-04",
                "2017-05-09"
            ]
        }
    ]
}

# extracting data in json format
data = r

print(data)
countries = dict()
dates = dict()
noOfPartneres = len(data['partners'])
for i in range(noOfPartneres):
    if data['partners'][i]['country'] in countries:
        countries[data['partners'][i]['country']].append(data['partners'][i]['availableDates'])
        countries[data['partners'][i]['country']].append(data['partners'][i]['email'])
    else:
        countries[data['partners'][i]['country']] = [data['partners'][i]['availableDates'],
                                                     data['partners'][i]['email']]
    # print(data['partners'][i]['country'])
print(countries)
print(len(countries))
for i in range(len(countries)):
    numOfRecords = len(countries[data['partners'][i]['country']])
    # print(countries[data['partners'][i]['country']])
    temp = []
    for j in range(numOfRecords):
        if j % 2 == 0:
            temp.append(countries[data['partners'][i]['country']][j])

    # flat_list = [item for sublist in temp for item in sublist]
    # print(flat_list)

    # dates[data['partners'][i]['country']] = countries[data['partners'][i]['country']][j]

    # print(dates)
