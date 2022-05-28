
import requests
import pandas

def ingest(link):
    req = requests.get(link)
    file = req.json()['data']

    list_data = []
    for data in file:
        dict_data = {}
        dict_data['UserId'] = data['User']
        dict_data['UserFirst'] = data['context'][0]['first']
        dict_data['UserLast'] = data['context'][0]['last']
        list_data.append(dict_data)
    df = pandas.DataFrame(list_data)
    return df