# blocker.py
import subprocess

def block_ip(ip_address):
    """
    Blocks the given IP address using Windows Firewall.
    """
    rule_name = f"BlockSpoof_{ip_address}"
    try:
        subprocess.run([
            "netsh", "advfirewall", "firewall", "add", "rule",
            "name=", rule_name,
            "dir=in", "action=block", "remoteip=", ip_address,
            "enable=yes"
        ], check=True)
        print(f"[INFO] Blocked IP {ip_address} via Windows Firewall.")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to block IP {ip_address}: {e}")
