import pandas as pd
import datetime
from unvrs_list import unvrs
import requests
import urllib3

# Suppress HTTPS warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# List to hold cameras that are down
down_cameras = []

for unvr in unvrs:
    nvr_name = unvr["name"]
    nvr_ip = unvr["ip"]
    api_key = unvr["api_key"]

    if not nvr_ip or not api_key:
        continue

    url = f"https://{nvr_ip}/proxy/protect/integration/v1/cameras"
    headers = {"X-API-KEY": api_key, "Accept": "application/json"}

    try:
        response = requests.get(url, headers=headers, verify=False)
        response.raise_for_status()
        cameras = response.json()

        for cam in cameras:
            state = cam.get("state", "Unknown")
            if state != "CONNECTED":  # Only log disconnected cameras
                down_cameras.append({
                    "Site Name": nvr_name,
                    "NVR IP": nvr_ip,
                    "Camera Name": cam.get("name", "Unknown"),
                    "Camera State": state,
                    "Last Checked": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to {nvr_name} ({nvr_ip}): {e}")

# Save only the disconnected cameras to Excel
if down_cameras:
    df = pd.DataFrame(down_cameras)
    df.to_excel("disconnected_cameras.xlsx", index=False)
    print("Saved disconnected cameras to disconnected_cameras.xlsx")
else:
    print("All cameras are connected. No disconnected cameras to report.")