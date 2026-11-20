# Packages my beloved
import sys
import time
import json

import httpx  # type: ignore

# Loading JSON stuff
with open("config.json", "r") as file:
    config = json.load(file)
    
# Variables and crap
CAR_API = "https://alerts.globaleas.org/api/v2/"
monitored = config["monitored"]

def clear():
    # This just clears the terminal output
    print("\033[2J\033[H", end="")
    # MAY BE COMMENTED OUT FOR DEBUGGING PURPOSES
    pass

def writeJSON(input, file="config.json"):       
    with open(file, "w+") as output:
        json.dump(input, output, indent=4)

def showAlerts(alerts):
    for number, alert in enumerate(alerts, start=1):
        clear()
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
    
# Getting active alerts
r = httpx.get(CAR_API + "alerts/active")
activeAlerts = r.json()

# Main program
try:
    while True:
        clear()
        alerts = []
        choice = ""
        
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
            if len(activeAlerts) == 0:
                print("No active alerts.")
                time.sleep(2)
                continue
            for alert in activeAlerts:
                if any(code in monitored for code in alert["fipsCodes"]):
                    alerts.append(alert)
            clear()
            showAlerts(alerts)
        elif choice == "2":
            if len(activeAlerts) == 0:
                print("No active alerts.")
                time.sleep(2)
                continue
            alerts = activeAlerts
            clear()
            showAlerts(alerts)
        elif choice == "3":
            while True:
                clear()
                print("Enter one 6-digit FIPS code at a time. Enter nothing to exit.")
                print("!! IF YOU ENTER CODES THAT AREN'T ASSIGNED TO COUNTIES, FILTERING ALERTS WILL NOT WORK !!")
                code = input("==> ")
                if len(code) == 0:
                    break
                elif not code.isdecimal():
                    print("Please enter a 6-digit FIPS code.") 
                    time.sleep(1)
                elif len(code) == 6:
                    if code not in monitored:
                        monitored.append(code)
                        writeJSON({"monitored": monitored})
                    else:
                        print("That FIPS code is already being monitored.")
                        time.sleep(1)
                else:
                    print("Please enter a 6-digit FIPS code.")
                    time.sleep(1)
        elif choice == "4":
            while True:
                clear()
                if len(monitored) == 0:
                    print("No FIPS codes to remove")
                    time.sleep(1)
                    break
                print("Enter one 6-digit FIPS code to remove at a time. Enter nothing to exit.")
                code = input("==> ")
                if len(code) == 0:
                    break
                elif not code.isdecimal():
                    print("Please enter a 6-digit FIPS code to remove.") 
                    time.sleep(1)
                elif len(code) == 6:
                    if code not in monitored:
                        print("That FIPS code is already unmonitored.")
                        time.sleep(1)
                    else:
                        monitored.remove(code)
                        writeJSON({"monitored": monitored})
                else:
                    print("Please enter a 6-digit FIPS code.")
                    time.sleep(1)
        elif choice == "5":
            while True:
                clear()
                if len(monitored) == 0:
                    print("No FIPS codes to clear")
                    time.sleep(1)
                    break
                print("Are you sure you want to clear FIPS codes? (y/N)")
                clearConfirm = input("==> ").lower()
                if clearConfirm == "y":
                    monitored = []
                    writeJSON({"monitored": monitored})
                    break
                elif clearConfirm == "n" or len(clearConfirm) == 0:
                    break
                else:
                    pass
        elif choice == "6":
            clear()
            break
except KeyboardInterrupt:
    clear()
    sys.exit()