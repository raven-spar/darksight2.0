import json
import requests

def mail_pass(mail):
    url = "https://api.proxynova.com/comb?query="
    response = requests.get(url+mail)
    data = json.loads(response.text)["lines"]
    pass_list = []
    for i in data:
        if (i.split(":")[0] == mail):
            pass_list.append(i.split(":")[1])
    return pass_list

def password(password):
    url = "https://api.proxynova.com/comb?query="
    response = requests.get(url+password)
    data = json.loads(response.text)["lines"]
    for i in data:
        if (i.split(":")[1] == password):
            return True
    return False

def breaches():
    url = "https://haveibeenpwned.com/api/v2/breaches"
    response = requests.get(url)
    data = json.loads(response.text)
    # for i in data:
    #     name, domain, date, count, description = i["Name"], i["Domain"], i["BreachDate"], 
    #     domain = i["Domain"]
    #     date = i["BreachDate"]
    #     count = i["PwnCount"]
    #     description = i["Description"]
    #     print(name, domain, )
    #     break
    return json.dumps(data)



