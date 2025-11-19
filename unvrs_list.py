import os
from dotenv import load_dotenv

# Load environment variables from example file
load_dotenv(dotenv_path="unvrs.env")

# Dummy UniFi NVR list for demo purposes (NO real IPs or keys)
unvrs = [
    {"name": "Site Alpha","ip": os.getenv("UNVR_SITE_ALPHA_IP"),"api_key": os.getenv("UNVR_SITE_ALPHA_KEY")},
    {"name": "Site Bravo","ip": os.getenv("UNVR_SITE_BRAVO_IP"),"api_key": os.getenv("UNVR_SITE_BRAVO_KEY")},
]
