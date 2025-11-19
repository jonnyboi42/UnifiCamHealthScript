import os
from dotenv import load_dotenv

# Load environment variables from example file
load_dotenv(dotenv_path="unvrs.env")

# Dummy UniFi NVR list for demo purposes (NO real IPs or keys)
unvrs = [
    {"name": "Site Alpha","ip": os.getenv("UNVR_SITE_ALPHA_IP"),"api_key": os.getenv("UNVR_SITE_ALPHA_KEY")},
    {"name": "Site Bravo","ip": os.getenv("UNVR_SITE_BRAVO_IP"),"api_key": os.getenv("UNVR_SITE_BRAVO_KEY")},
    {"name": "Site Charlie","ip": os.getenv("UNVR_SITE_CHARLIE_IP"),"api_key": os.getenv("UNVR_SITE_CHARLIE_KEY")},
    {"name": "Site Delta","ip": os.getenv("UNVR_SITE_DELTA_IP"),"api_key": os.getenv("UNVR_SITE_DELTA_KEY")},
    {"name": "Site Echo","ip": os.getenv("UNVR_SITE_ECHO_IP"),"api_key": os.getenv("UNVR_SITE_ECHO_KEY")},
    {"name": "Site Foxtrot","ip": os.getenv("UNVR_SITE_FOXTROT_IP"),"api_key": os.getenv("UNVR_SITE_FOXTROT_KEY")},
    {"name": "Site Gamma","ip": os.getenv("UNVR_SITE_GAMMA_IP"),"api_key": os.getenv("UNVR_SITE_GAMMA_KEY")},
    {"name": "Site Horizon","ip": os.getenv("UNVR_SITE_HORIZON_IP"),"api_key": os.getenv("UNVR_SITE_HORIZON_KEY")},
    {"name": "Site Ironwood","ip": os.getenv("UNVR_SITE_IRONWOOD_IP"),"api_key": os.getenv("UNVR_SITE_IRONWOOD_KEY")},
    {"name": "Site Juniper","ip": os.getenv("UNVR_SITE_JUNIPER_IP"),"api_key": os.getenv("UNVR_SITE_JUNIPER_KEY")},
]
