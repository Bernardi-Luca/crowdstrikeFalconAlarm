import os
from datetime import date
import yaml
from CrowdClient.crowdclient import CrowdClient
from telegram import *
import win10toast


def writeDetectionToFile(text, customer):
    text = customer + " - " + str(text).split("'max_severity_displayname': '")[1].split("',")[0]
    
    print(text)
    print(
        "=========================")
    detectionsFile.write(str(text))
    detectionsFile.write(
        "=========================")
    #win10toast.ToastNotifier().show_toast("falcon detection", str(text))
    send_message(str(text))


def getDetections():
    dict_detections = []
    today = date.today()
    try:
        for customer in customers:
            #print("processing customer --> " + customer)
            # customer is customer name
            # customers[customer] is a list of key value pairs of clients and secrets
            customerClientKey = customers[customer].get("client")
            customerSecretKey = customers[customer].get("secret")
            # print(customer, customerClientKey, customerSecrettKey)

            # handling auth to falcon for each customer
            client = CrowdClient(customerClientKey, customerSecretKey)
            client.authenticate()
            detections = client.get_detections()
            #incidents = client.get_incidents()
            detectionDetails = client.get_detection_details(detections)
            #incidentDetails = client.get_incident_details(incidents)

            # for detail_inc in incidentDetails:
            #     print(detail_inc)
            #     if str(detail_inc['created_timestamp']).startswith(str(today)) and detail_inc['status'] == 'new':
            #         writeDetectionToFile(detail_inc)

            for detail_det in detectionDetails:
                #if str(detail_det['created_timestamp']).startswith(str(today)) and detail_det['status'] == 'new':
                if detail_det['status'] == 'new':
                    writeDetectionToFile(detail_det, customer)

            # dumpedDetections = yaml.dump(detections)

            # return dumpedDetections
    except:
        print("catched execution error")


if os.path.isfile("settings.yml") and os.path.isfile("customers.yml"):

    settingsFile = open(r'settings.yml', 'r')
    customersFile = open('customers.yml', 'r')
    detectionsFile = open('detections.txt', 'w')
    customers = yaml.load(customersFile, Loader=yaml.FullLoader)
    settings = yaml.load(settingsFile, Loader=yaml.FullLoader)
