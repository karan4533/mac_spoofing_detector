# MAC Spoofing Detection Tool

## Description
This tool monitors ARP traffic to detect MAC address spoofing on a local network.

## Features
- Live ARP monitoring
- MAC spoofing alerts
- Logs suspicious activity

## Setup
```bash
pip install -r requirements.txt
```

## Usage
```bash
python main.py
```

## Notes
- Run with admin/root privileges for packet sniffing.
- Modify `config.py` to set your network interface.
- Default timeout is 30 seconds; adjust in `start_sniffing()` for longer scans.
- Configure your Gmail app password in `email_config.py`
