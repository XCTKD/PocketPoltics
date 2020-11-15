## Adam E. Farence ##
## Pocket Politics V.1 ##
## 11.04.2020 ##

import requests
import csv

# url = "https://api.open.fec.gov/v1/candidates/search/?year=2020&sort_nulls_last=true&candidate_status=&sort=name&per_page=20&sort_hide_null=false&sort_null_only=false&api_key=U8BzrfhKCYJg0conOwlfwvQtcIor8FKmQhGii14o&page=1"

# response = requests.get(url, allow_redirects=True)
# data = response.json()
# print(response)
# print(data.keys())
# candidate_id_layer = data['results']
# print(candidate_id_layer[0])
# # #print(candidate_id_layer)
# # for candidate in candidate_id_layer:
# #     print(candidate_id_layer['candidate_id'])

### CANDIDATE STUFF ###

url = "https://api.open.fec.gov/v1/candidate/P80001571?api_key=U8BzrfhKCYJg0conOwlfwvQtcIor8FKmQhGii14o"
DTresponse = requests.get(url, allow_redirects=True)
data = DTresponse.json()
print(DTresponse)
# print(data.keys())
layer1 = data['results']
# for result in layer1:
#     print(result.keys())

x = layer1[0]
print(x.keys())
# for y in x:
#     print(x.keys())
print('----')
print(x['name'])
print('----')
print(x['party'])
print('----')
print(x['federal_funds_flag'])
print('----')
print(x['party_full'])

url2 = "https://api.open.fec.gov/v1/candidate/P80001571/totals?api_key=U8BzrfhKCYJg0conOwlfwvQtcIor8FKmQhGii14o"
Tresponse = requests.get(url2, allow_redirects=True)
Tdata = Tresponse.json()
totals_layer1 = Tdata['results']
iic = totals_layer1[0]['individual_itemized_contributions']

### COMMITTEE STUFF ###

url3 = "https://api.open.fec.gov/v1/committee/C00580100/totals?api_key=U8BzrfhKCYJg0conOwlfwvQtcIor8FKmQhGii14o"
response3 = requests.get(url3, allow_redirects=True)
data_3 = response3.json()
print('----')
print('----')
print('----')
print(data_3.keys())
committee_layer_1 = data_3['results']
print(committee_layer_1[0])
print('----')
print('----')
print('----')
## PRINT LOGIC HERE ##
print(f"{x['name']}, of the {x['party_full']}, has received ${iic:,} in\nindividual itemized contributions while running for the office of {x['office_full']}.")

## WRITE TO CSV FILE ##

# with open('APItest.csv',newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row['first_name'], row['last_name'])

# print(row)

# f = open('Users\aefar\IntroToComputing\OtherProjects\APItest.csv',"w")
# f.write(data.text)
# f.close()