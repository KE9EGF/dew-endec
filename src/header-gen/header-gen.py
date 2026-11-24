import datetime as dt  # noqa: F401, I001, RUF100 <== absolute ridiculousness right here folks
import sys
import time  # noqa: F401

alertTypes = {
    "ADR": "Administrative Message",
    "AVA": "Avalanche Watch",
    "AVW": "Avalanche Warning",
    "BHW": "Biological Hazard Warning",
    "BWW": "Boil Water Warning",
    "BZW": "Blizzard Warning",
    "CAE": "Child Abduction Emergency",
    "CDW": "Civil Danger Warning",
    "CEM": "Civil Emergency Message",
    "CFA": "Coastal Flood Watch",
    "CFW": "Coastal Flood Warning",
    "CFS": "Coastal Flood Statement",
    "DBA": "Dam Watch",
    "DBW": "Dam Break Warning",
    "DMO": "Practice/Demo Warning",
    "DSA": "Dust Advisory",
    "DSW": "Dust Storm Warning",
    "EAN": "Emergency Action Notification",
    "EAT": "Emergency Action Termination",
    "EVI": "Evacuation Immediate",
    "EWW": "Extreme Wind Warning",
    "FFA": "Flash Flood Watch",
    "FFS": "Flash Flood Statement",
    "FFW": "Flash Flood Warning",
    "FLA": "Flood Watch",
    "FLS": "Flood Statement",
    "FLW": "Flood Warning",
    "FRW": "Fire Warning",
    "HMW": "Hazardous Materials Warning",
    "HLS": "Hurricane Local Statement",
    "HUA": "Hurricane Watch",
    "HUW": "Hurricane Warning",
    "HWA": "High Wind Watch",
    "HWW": "High Wind Warning",
    "IBW": "Iceberg Warning",
    "LAE": "Local Area Emergency",
    "LEW": "Law Enforcement Warning",
    "LES": "Lake Effect Snow Warning",
    "NIC": "National Information Center",
    "NMN": "Network Message Notification",
    "NPT": "National Periodic Test",
    "NUW": "Nuclear Power Plant Warning",
    "POS": "Power Outage Statement",
    "RHW": "Radiological Hazard Warning",
    "RFW": "Red Flag Warning",
    "RMT": "Required Monthly Test",
    "RWT": "Required Weekly Test",
    "SMW": "Special Marine Warning",
    "SPS": "Special Weather Statement",
    "SPW": "Shelter in Place Warning",
    "SSA": "Storm Surge Watch",
    "SSW": "Storm Surge Warning",
    "SVA": "Severe Thunderstorm Watch",
    "SVR": "Severe Thunderstorm Warning",
    "SVS": "Severe Weather Statement",
    "TOA": "Tornado Watch",
    "TOE": "911 Telephone Outage Emergency",
    "TOR": "Tornado Warning",
    "TRA": "Tropical Storm Watch",
    "TRW": "Tropical Storm Warning",
    "TSA": "Tsunami Watch",
    "TSW": "Tsunami Warning",
    "TYA": "Typhoon Watch",
    "TYW": "Typhoon Warning",
    "VOW": "Volcano Warning",
    "WSA": "Winter Storm Watch",
    "WSW": "Winter Storm Warning",
    "WWA": "Winter Weather Advisory",
}


def clear():
    # This just clears the terminal output
    print("\033[2J\033[H", end="")
    # MAY BE COMMENTED OUT FOR DEBUGGING PURPOSES


try:
    while True:
        clear()
        print("HEADER-GEN\n")
        print("""
        1. Encode a Header
        2. Decode a Header
        3. Exit      
        """)
except KeyboardInterrupt:
    sys.exit()
