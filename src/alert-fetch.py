import httpx
import json
import datetime as dt
import sys
import time

CAR_API = "https://alerts.globaleas.org/api/v2/"

r = httpx.get(CAR_API + "alerts/active")

alerts = r.json()
number = 1

try:
    for alert in alerts:
        print(f"""
        Alert #{number}
        Type:        {alert["type"]}
        Severity:    {alert["severity"]}
        Start Time:  {alert["startTime"]}
        End Time:    {alert["endTime"]}
        SAME Header: {alert["protocolHeader"]}
        Message:     {alert["translation"]}
        """)
        input("")
        number += 1
    print("No more alerts.")
    time.sleep(2)
    sys.exit()
except KeyboardInterrupt:
    sys.exit()