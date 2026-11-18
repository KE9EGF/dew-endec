# Paclages my beloved
import sys
import time

import httpx  # type: ignore

# Variables and crap
CAR_API = "https://alerts.globaleas.org/api/v2/"
monitored = [
    "000000",  # Don't remove unless you don't want nationwide alerts to show
    "036103",
]

# Getting active alerts for specified FIPS codes
r = httpx.get(CAR_API + "alerts/active")
activeAlerts = r.json()
alerts = []
for alert in activeAlerts:
    if any(code in monitored for code in alert["fipsCodes"]):
        alerts.append(alert)

print(activeAlerts)

# Main program
try:
    if len(alerts) == 0:
        print("No active alerts.")
        time.sleep(2)
        sys.exit()

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
