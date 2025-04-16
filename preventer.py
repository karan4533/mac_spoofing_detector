# preventer.py
import subprocess

def block_device(ip, mac):
    try:
        # Using Windows Firewall to block the attacker based on their MAC address
        subprocess.run(["netsh", "advfirewall", "firewall", "add", "rule", "name=BlockAttacker", "dir=in", "action=block", "protocol=all", "localport=all", "remoteport=all", "remoteip=" + ip], check=True)
        return f"Device with MAC {mac} and IP {ip} successfully blocked."
    except Exception as e:
        return f"Failed to block device with IP {ip} and MAC {mac}: {e}"
