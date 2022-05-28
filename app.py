#!python3

import os
import api_ingest
import csv_ingest


if __name__=="__main__":
    print("Starting Ingest...")

    path_data = os.getcwd() + "\\dataset\\"
    link = open(path_data + 'API_Json.txt','r').read()
    csv_order = path_data + 'TR_OrderDetails.csv'
    csv_product = path_data + 'TR_Products.csv'
    csv_property = path_data + 'TR_PropertyInfo.csv'
    csv_user = path_data + 'TR_UserInfo.csv'

    data = api_ingest.ingest(link)
    order = csv_ingest.ingest(csv_order)
    product = csv_ingest.ingest(csv_product)
    property = csv_ingest.ingest(csv_property)
    user = csv_ingest.ingest(csv_user)

    print(user)
    print("Ingest Finished...")