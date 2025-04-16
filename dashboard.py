import streamlit as st

def display_status(spoof_detected, block_status):
    # Title and header
    st.title("🛡️ MAC Spoofing Detection Dashboard")
    st.header("📡 Real-Time Network Monitoring")

    # Detection result
    if spoof_detected:
        st.subheader("🚨 Alert: MAC Spoofing Detected!")
        st.markdown("### 🔒 Blocked Device Details")
        st.markdown(f"""
        - **IP Address**     : `{block_status.get('ip_address', 'Unknown')}`  
        - **MAC Address**    : `{block_status.get('mac_address', 'Unknown')}`  
        - **Blocked Status** : `{block_status.get('blocked', 'Unknown')}`  
        """)
        st.markdown("---")
    else:
        st.subheader("✅ Status: No MAC Spoofing Detected")
        st.markdown("Everything looks secure. No suspicious activity detected.")
        st.markdown("---")

    # Sidebar system info
    st.sidebar.header("🖥️ System Info")
    st.sidebar.text(f"IP Address: {block_status.get('ip_address', 'Unknown')}")
    st.sidebar.text(f"MAC Address: {block_status.get('mac_address', 'Unknown')}")

    # Sidebar logs
    st.sidebar.subheader("📜 Logs")
    st.sidebar.text("Last Status: Spoofing detected" if spoof_detected else "No spoofing detected")

# For manual testing only — not used in integration
if __name__ == '__main__':
    spoof_detected = True
    block_status = {
        'ip_address': '192.168.1.100',
        'mac_address': '00:11:22:33:44:55',
        'blocked': 'Yes'
    }
    display_status(spoof_detected, block_status)
