import requests

USERNAME = "ramsiyaram"
TOKEN = "lskhkjgjhfhgfhgdfgf"
GRAPH_ID = "graph2"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

#response = requests.post(url=pixela_endpoint,json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}graphs"

graph_config = {
    "id" : GRAPH_ID,
    "name" : "Coding Graph",
    "unit" : "Min",
    "type" : "float",
    "color" : "ajisai"
}

headers = {
    "X-USER-TOKEN" : TOKEN,
}

#response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
#print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date" : "20230609",
    "quantity" : "1.4",
}


response = requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)
print(response.text)