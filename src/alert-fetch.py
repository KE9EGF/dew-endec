import httpx
import json
import datetime as dt
import sys
import time

CAR_API = "https://alerts.globaleas.org/api/v2/"

r = httpx.get(CAR_API + "alerts/active")

alerts = r.json()

try:
    if len(alerts) == 0:
        print("No active alerts.")
        time.sleep(2)
        sys.exit
    
    for number, alert in enumerate(alerts, start=1):
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
    print("No more alerts.")
    time.sleep(2)
    sys.exit()
except KeyboardInterrupt:
    sys.exit()