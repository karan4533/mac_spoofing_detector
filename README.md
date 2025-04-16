Here's the **properly structured and formatted `README.md` file** incorporating all your content — polished for GitHub, including correct markdown headers, syntax highlighting, and readability:

---

```markdown
# 🛡️ MAC Spoofing Detection Tool

## 📄 Overview

A Python-based network security tool that monitors ARP traffic to detect MAC address spoofing on a local network. When spoofing is detected, it sends an email alert, blocks the attacker’s IP using Windows Firewall, and updates a live dashboard built with Streamlit.

---

## 🚀 Features

- 🔍 Real-time ARP Packet Sniffing
- ⚠️ MAC Spoofing Detection & Logging
- 📧 Email Alerts via Gmail
- 🔒 Automatic Blocking via Windows Firewall (Windows only)
- 📊 Live Dashboard using Streamlit

---

## 🧰 Technologies Used

| Technology        | Purpose                                 |
|------------------|-----------------------------------------|
| **Python**        | Core programming language               |
| **Scapy**         | Sniffing ARP packets                    |
| **Streamlit**     | Web dashboard UI                        |
| **smtplib**       | Email notification system               |
| **Windows Firewall (netsh)** | Blocking attacker IP automatically   |
| **Threading**     | Simultaneous sniffing & dashboard       |

---

### 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/mac-spoofing-detector.git
cd mac-spoofing-detector
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure the Tool

Set your **network interface** in `config.py`:

```python
INTERFACE = "Wi-Fi"  # or "Ethernet"
```

Set your **email credentials** in `email_config.py` (use a Gmail app password):

```python
EMAIL_ADDRESS = "your-email@gmail.com"
EMAIL_PASSWORD = "your-app-password"
```

---

## ▶️ Usage

Run the main application:

```bash
python main.py
```

> ⚠️ Make sure to **run with admin/root privileges** (Right-click > "Run as Administrator" on Windows).

By default, the tool:
- Sniffs ARP packets for **30 seconds** (modifiable in `arp_sniffer.py`)
- Sends **email alerts** if spoofing is detected
- **Blocks** attacker IP via Windows Firewall
- Updates a **live dashboard** using Streamlit

---

## 📺 Streamlit Dashboard Preview

The Streamlit dashboard displays:

- 🔄 Real-time spoofing detection status
- 🔍 Spoofed device details (IP, MAC, Block Status)
- 🖥️ System Info and Logs in Sidebar

To run the dashboard manually (optional):

```bash
streamlit run dashboard.py
```

---

## ✉️ Email Alert Format

### 🔴 When Spoofing is Detected:

```yaml
🚨 MAC Spoofing Detected!

🔒 Blocked Device Details:
📍 IP Address: 192.168.1.100
🖥️ MAC Address: 00:11:22:33:44:55
🚫 Blocked Status: Yes
```

---

### 🟢 When No Spoofing is Detected:

```yaml
✅ No MAC spoofing detected in your system.

🔒 Blocked Device Details:
📍 IP Address: N/A
🖥️ MAC Address: N/A
🚫 Blocked Status: No spoofing
```

---

## 📁 Project Structure

```bash
mac-spoofing-detector/
│
├── arp_sniffer.py       # Core ARP sniffer and detector
├── detector.py          # Spoofing detection logic
├── preventer.py         # Windows firewall blocker
├── logger.py            # Email alert system
├── dashboard.py         # Streamlit UI
├── main.py              # Main entry point
├── config.py            # Network interface config
├── email_config.py      # Email credentials
├── requirements.txt     # Dependencies list
```

---

## 📌 Notes

- ✅ Tested on **Windows OS** for firewall blocking.
- 🔐 Run as administrator to allow sniffing and firewall rules.
- ⏱️ Modify sniffing duration in `start_sniffing()` inside `arp_sniffer.py`.

---

## 🔒 Disclaimer

> This project is intended for **educational and research** use only.  
> Do **not** run on public or unauthorized networks without permission.

---

## ✅ Author

Developed as part of a **Network Security Project** on MAC spoofing detection and prevention using Python, Streamlit, and Windows Firewall.

---

## 🧪 Sample `requirements.txt`

```txt
scapy
streamlit
```

---

Let me know if you'd like to add GitHub badges (e.g., Python version, License, Last Commit) or include screenshots of the dashboard!
```

---

✅ **To Use**: Save this as `README.md` in the root of your project, and GitHub will render it perfectly.

Want me to generate GitHub badges or create a LICENSE too?