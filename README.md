# 🛡️ MAC Spoofing Detection Tool

## 📄 Overview

The **MAC Spoofing Detection Tool** is a Python-based network security application designed to monitor real-time ARP traffic to detect and prevent MAC address spoofing attacks on a local network. It provides live email alerts, blocks spoofers via Windows Firewall, and includes a live dashboard built with Streamlit.

---

## 🚀 Features

- 🔍 Real-time ARP Packet Sniffing
- ⚠️ Spoofing Detection & Logging
- 📧 Email Notifications (with spoofing status)
- 🔒 Automatic IP Blocking via Windows Firewall
- 📊 Live Web Dashboard (Streamlit)
- 💬 Console Output for Debugging

---

## 🧰 Tools & Technologies Used

| Technology      | Purpose                                             |
|------------------|-----------------------------------------------------|
| **Python**        | Main programming language                          |
| **Scapy**         | Packet sniffing and ARP spoofing detection         |
| **Streamlit**     | Live dashboard display of spoofing alerts          |
| **smtplib**       | Sending email alerts via Gmail                     |
| **Windows Firewall** (`netsh`) | Automatically block spoofing devices       |
| **Threading**     | Concurrent sniffer and dashboard execution         |

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/mac-spoofing-detector.git
cd mac-spoofing-detector

2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Configure the Tool
Set your network interface in config.py:

python
Copy
Edit
INTERFACE = "Wi-Fi"  # or "Ethernet"
Set your email credentials in email_config.py (use a Gmail app password):

python
Copy
Edit
EMAIL_ADDRESS = "your-email@gmail.com"
EMAIL_PASSWORD = "your-app-password"
▶️ Usage
Run the main application:

bash
Copy
Edit
python main.py
Make sure to run with admin/root privileges (Right-click > Run as Administrator on Windows).

The tool starts sniffing ARP packets for 30 seconds by default (customizable in arp_sniffer.py).

If spoofing is detected:

Email alert is sent 📧

Attacker's IP is blocked via Windows Firewall 🔥

Dashboard shows alert 🚨

If no spoofing is detected:

Safe status email is sent ✅

Dashboard shows “No Spoofing Detected” 🟢

📺 Streamlit Dashboard Preview
The Streamlit dashboard displays:

🔄 Real-time spoofing detection status

🔍 Blocked device details (IP, MAC, Blocked Status)

🖥️ System info & logs in sidebar

Run the dashboard manually (optional):

bash
Copy
Edit
streamlit run dashboard.py
✉️ Email Alert Format
When Spoofing is Detected:
yaml
Copy
Edit
🚨 MAC Spoofing Detected!

🔒 Blocked Device Details:
📍 IP Address: 192.168.1.100
🖥️ MAC Address: 00:11:22:33:44:55
🚫 Blocked Status: Yes
When No Spoofing is Detected:
yaml
Copy
Edit
✅ No MAC spoofing detected in your system.

🔒 Blocked Device Details:
📍 IP Address: N/A
🖥️ MAC Address: N/A
🚫 Blocked Status: No spoofing