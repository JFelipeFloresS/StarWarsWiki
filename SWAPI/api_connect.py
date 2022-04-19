import requests
import json

def get_json(category):
    c = category
    if category == "CHARACTERS":
        c = "PEOPLE"
    response = requests.get("https://swapi.dev/api/" + c.lower() + "/")
    return response.json()

def get_selected(url):
    response = requests.get(url)
    return response.json()

def get_subset(sets):
    print(sets)
    resident_json = {}
    for s in sets:
        response = requests.get(s)
        resident_json[s] = (response.json())

    return resident_json
