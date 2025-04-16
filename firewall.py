# firewall.py
import subprocess

def block_ip(ip):
    print(f"[INFO] Blocking IP {ip} from accessing the network.")
    try:
        subprocess.run(
            ["netsh", "advfirewall", "firewall", "add", "rule", "name=BlockSpoof_" + ip,
             "dir=in", "action=block", "remoteip=" + ip, "enable=yes"],
            check=True
        )
        print(f"[INFO] Successfully blocked IP {ip} using Windows Firewall.")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to block IP {ip}: {e}")
if __name__ == "__main__":
    block_ip("192.168.1.123")  # replace with a dummy IP for testing
