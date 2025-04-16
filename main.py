# main.py
import subprocess
from arp_sniffer import start_sniffing
import threading

def start_dashboard():
    subprocess.run(["python", "-m", "streamlit", "run", "dashboard.py"])

if __name__ == '__main__':
    print("[INFO] Starting MAC Spoofing Detector...")

    dashboard_thread = threading.Thread(target=start_dashboard)
    dashboard_thread.start()

    start_sniffing()
