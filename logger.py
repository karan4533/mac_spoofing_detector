# logger.py (Updated email content)

import datetime
import smtplib
from email.message import EmailMessage
from email_config import EMAIL_ADDRESS, EMAIL_PASSWORD, TO_EMAIL, SMTP_SERVER, SMTP_PORT

def log_alert(message, block_status):
    with open("alerts.log", "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {message}\n")
    send_email_alert(message, block_status)

def send_email_alert(message, block_status):
    try:
        msg = EmailMessage()
        msg.set_content(f"""
        Dear User,

        We have detected a MAC Spoofing attempt on your network.

        Alert Details:
        {message}

        Block Status: {block_status}

        This is an automated alert from the MAC Spoofing Detection System.

        Best regards,
        MAC Spoofing Detection Team
        """)
        
        msg["Subject"] = "MAC Spoofing Alert Detected"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = TO_EMAIL

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("[DEBUG] Email sent successfully!")
    except Exception as e:
        print(f"[ERROR] Failed to send email: {e}")
