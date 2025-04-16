# detector.py
import logger
from utils import ip_mac_table
import preventer  # 🆕

def check_spoof(ip, mac):
    if ip in ip_mac_table:
        if ip_mac_table[ip] != mac:
            warning = f"[ALERT] Possible MAC Spoofing Detected: IP {ip} changed from {ip_mac_table[ip]} to {mac}"
            print(warning)
            logger.log_alert(warning)
            
            # 🧱 Block the attacker
            if preventer.block_ip(ip):
                logger.log_alert(f"[BLOCKED] IP {ip} has been blocked.")

            return True
    else:
        ip_mac_table[ip] = mac
    return False
