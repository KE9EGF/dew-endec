# Paclages my beloved
import sys
import time
import json

import httpx  # type: ignore

# Variables and crap
CAR_API = "https://alerts.globaleas.org/api/v2/"
new = {
    "monitored": ['000000']
}

def clear():
    # This just clears the terminal output
    print("\033[2J\033[H", end="")

def writeJSON(file, input):       
    with open(file, "w+") as output:
        json.dump(input, output, indent=4)
        
# Loading JSON stuff
with open("config.json", "r") as file:
    config = json.load(file)

writeJSON("config.json", new)

# Getting active alerts
r = httpx.get(CAR_API + "alerts/active")
activeAlerts = r.json()
alerts = []

# Main program
try:
    while True:
        clear()
        print("ALERT-FETCH\n")
        print("""
        1. Alerts from FIPS Codes
        2. All Active Alerts
        3. Add a FIPS Code
        4. Remove a FIPS Code
        5. Clear FIPS Codes
        6. Exit
        """)
        choice = input("==> ")
        if choice == "1":
            for alert in activeAlerts:
                if any(code in monitored for code in alert["fipsCodes"]):
                    alerts.append(alert)
        elif choice == "2":
            alerts = activeAlerts
        elif choice == "3":
            clear()
            print("Enter one 5-digit FIPS code at a time. Enter nothing to exit.")
            print("IF YOU ENTER INVALID CODES, YOU WILL NOT BE ABLE TO FILTER ALERTS!")
            code = input("==> ")
            try:
                code = int(code)
            except ValueError:
                print("Please enter a 5-digit FIPS code.")
                time.sleep(1)
            if len(code) == 5:
                pass
        if len(activeAlerts) == 0:
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
            clear()
        print("No more alerts.")
        time.sleep(2)
        sys.exit()
except KeyboardInterrupt:
    clear()
    sys.exit()



