# arp_sniffer.py
from scapy.all import sniff, ARP
from detector import check_spoof
from config import INTERFACE
import logger
import preventer

no_spoofing = True
block_status = {}

def process_packet(packet):
    global no_spoofing, block_status

    if packet.haslayer(ARP) and packet[ARP].op == 2:
        ip = packet[ARP].psrc
        mac = packet[ARP].hwsrc

        if check_spoof(ip, mac):
            no_spoofing = False
            block_status = preventer.block_device(ip, mac)
            message = "🚨 MAC Spoofing Detected!\n\n🔒 Blocked Device Details:\n" \
                      f"📍 IP Address: {block_status.get('ip_address', 'Unknown')}\n" \
                      f"🖥️ MAC Address: {block_status.get('mac_address', 'Unknown')}\n" \
                      f"🚫 Blocked Status: {block_status.get('blocked', 'Unknown')}"
            logger.send_email_alert(message, block_status)

def start_sniffing():
    global block_status

    try:
        print("[INFO] Starting ARP packet sniffing...")
        sniff(store=False, prn=process_packet, iface=INTERFACE, timeout=30)
    finally:
        if no_spoofing:
            print("[INFO] No MAC spoofing detected in your system.")
            # Send the default block status with "No spoofing detected"
            default_status = {
                'ip_address': 'N/A',
                'mac_address': 'N/A',
                'blocked': 'No spoofing'
            }
            logger.send_email_alert("✅ No MAC spoofing detected in your system.", default_status)
        else:
            print(f"[INFO] MAC spoofing detected. Block Status: {block_status}")
            # Send the actual block status for spoofing detection
            logger.send_email_alert("🚨 MAC Spoofing Detected!", block_status)

