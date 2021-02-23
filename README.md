this script fetches new detections from your falcon istance/s and sensd brief telegram messages with severity and istance name
used to get notifications for falcon detections with severity lower than medium.

uses crowdclient api
also outputs detections to file detections.txt in write mode and prints to terminal.

python3, requires:
pyYAML, 
CrowdClient, 
telepot

to make it work:
- generate bot, insert bot token and your number in telegram.py
- insert customer data in yml file
