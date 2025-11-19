# Unifi Camera Health Check Script

## Overview
This project automates the process of checking the status of cameras across multiple UniFi NVR (UNVR) locations. The script reports any cameras that are not connected and saves the results to an Excel file.

---

## Features
- Connects to multiple UNVRs using IP addresses and API keys.
- Checks the state of all cameras.
- Generates an Excel report for disconnected cameras.
- Can be run on a schedule (e.g., via Task Scheduler or cron).

---

## Setup

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create the `unvrs.env` file
You need to create a `.env` file called `unvrs.env` in the project folder with the IP and API key for each UNVR you want to monitor.  

Example:
```env
# UNVR Site 1
UNVR_SITE1_IP=192.168.1.121
UNVR_SITE1_KEY=REPLACE_ME

# UNVR Site 2
UNVR_SITE2_IP=192.168.1.122
UNVR_SITE2_KEY=REPLACE_ME
```

> Replace the IP addresses and keys with your actual UNVR information.

### 4. Load the UNVRs in `unvrs_list.py`
The `unvrs_list.py` file should import the environment variables and create a list of UNVRs:
```python
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="unvrs.env")

unvrs = [
    {"name": "Site 1", "ip": os.getenv("UNVR_SITE1_IP"), "api_key": os.getenv("UNVR_SITE1_KEY")},
    {"name": "Site 2", "ip": os.getenv("UNVR_SITE2_IP"), "api_key": os.getenv("UNVR_SITE2_KEY")},
]
```

---

## Usage
Run the script:
```bash
python camhealth.py
```

The script will:
1. Connect to each UNVR listed in `unvrs_list.py`.
2. Check the state of each camera.
3. Print any cameras that are disconnected.
4. Save the disconnected cameras to `disconnected_cameras.xlsx`.

---

## Notes
- The script uses `verify=False` for HTTPS requests to UNVRs. This suppresses certificate verification warnings.
- For security, **do not commit your real API keys** to GitHub. Use dummy values in your public repository.

---

## Dependencies
- Python 3.10+
- `requests`
- `pandas`
- `python-dotenv`
- `openpyxl`
