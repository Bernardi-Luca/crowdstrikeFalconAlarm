from falcon import *
import time
from datetime import datetime


if __name__ == '__main__':
    print("----- INIT -----")
    while True:
        print(datetime.now().strftime("%H:%M:%S") + " - tick")
        getDetections()
        time.sleep(120)
