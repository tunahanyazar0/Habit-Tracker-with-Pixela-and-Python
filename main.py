import requests
from datetime import datetime

USERNAME = "YOUR_USERNAME"
TOKEN = "YOUR_TOKEN"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"
TABLE_NAME = "Coding Graph"
UNIT = "Hour"
DATA_TYPE = "float"
PIXEL_COLOR =  "momiji"

#-------------------------- CREATING HEADERS----------------------------#
headers = {
    "X-USER-TOKEN" : TOKEN
}

#-------------------------- CREATING ACCOUNT----------------------------#
params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}
requests.post(url=pixela_endpoint,json=params)

#-------------------------- CREATING GRAPH----------------------------#
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : GRAPH_ID,
    "name" : TABLE_NAME,
    "unit" : UNIT,
    "type"  : DATA_TYPE,
    "color" : PIXEL_COLOR
}
requests.post(url=graph_endpoint, json=graph_config,headers=headers)

#-------------------------- REACHING GRAPH----------------------------#
# https://pixe.la/v1/users/USERNAME/graphs/GRAPH_ID.html

#-------------------------- CREATING  PIXELS----------------------------#
post_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.today()
today = today.strftime("%Y%m%d")

quantity_today = "2.0"

post_data_config = {
    "date"  : today,
    "quantity" : quantity_today
}
requests.post(url=post_endpoint,json=post_data_config,headers=headers)

#-------------------------- UPDATING PIXELS----------------------------#

date_to_change = datetime(year=2022,month=4,day=14)
date_to_change = date_to_change.strftime("%Y%m%d")

update_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{date_to_change}"

update_config = {
    "quantity"  : "2.0"
}
requests.put(url=update_endpoint,json=update_config,headers=headers)

#-------------------------- DELETING PIXELS----------------------------#
date_to_change2 = datetime(year=2022,month=4,day=14)
date_to_change2 = date_to_change2.strftime("%Y%m%d")

delete_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{date_to_change2}"
requests.delete(url=delete_endpoint,headers=headers)


