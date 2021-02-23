uses crowdclient api, which works quicker than falconpy

outputs detections to file detections.txt in write mode, prints to terminal, sends telegram message.
Gives minimum info, severity level and customer name.

python3, requires:
pyYAML, 
CrowdClient, 
telepot

to make it work:
- generate bot, insert bot token and your number in telegram.py
- insert customer data in yml file