
from ..utils.config_loader import load_config

def stream_processor(file_path):
    config = load_config(file_path)
    account = config['camera_01']['Account']
    password = config['camera_01']['Password']
    ip = config['camera_01']['IP']
    RTSP_URL = f"rtsp://{account}:{password}@{ip}:554/cam/realmonitor?channel=1&subtype=0"
    print(" Connection from camera following " , RTSP_URL)
    return RTSP_URL