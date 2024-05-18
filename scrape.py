import json
import requests

def mail_pass():
    url = "https://api.proxynova.com/comb?query="
    query = input("")

    response = requests.get(url+query)
    data = json.loads(response.text)["lines"]
    pass_list = []
    for i in data:
        if (i.split(":")[0] == query):
            pass_list.append(i.split(":")[1])
    return pass_list

def password():
    url = "https://api.proxynova.com/comb?query="
    query = input("")
    response = requests.get(url+query)
    data = json.loads(response.text)["lines"]
    for i in data:
        if (i.split(":")[1] == query):
            return True
    return False

def breaches():
    url = "https://haveibeenpwned.com/api/v2/breaches"
    response = requests.get(url)
    data = json.loads(response.text)
    return json.dumps(data, indent=5)



