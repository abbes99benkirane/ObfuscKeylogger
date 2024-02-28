# ObfuscKeylogger
# Overview
This document describes the functionality and operation of a sophisticated keylogger developed strictly for educational and ethical penetration testing purposes. The keylogger is crafted to monitor and log keystrokes on a system stealthily, then transmit the gathered data to a designated Discord webhook for analysis. It incorporates obfuscation techniques to minimize detection by security software and ensure its operations remain concealed.

# Key Features
**Stealth Mode Execution**: Through advanced obfuscation and persistence mechanisms, the keylogger disguises its presence on the system, ensuring continuous operation without detection.
**Discord Integration for Monitoring**: It utilizes a Discord webhook to send captured keystroke data, allowing for efficient remote monitoring.
**Automated Data Transmission**: Configured to send logged keystroke data at regular intervals (default is every 120 seconds) to the specified Discord channel.
**Customization Options**: Users have the flexibility to adjust the reporting interval and select the mode of data transmission, although the primary method is via webhook.

# Setup Instructions
**Prerequisites**: Ensure Python 3 and the necessary libraries (**keyboard**, **discord_webhook**, **shutil**, **subprocess**, **sys**) are installed on the target system.

```

pip install keyboard discord_webhook shutil subprocess sys

```

**Configure Discord Webhook**: You must create and configure a Discord webhook in the desired server/channel. Replace the WH variable in the script with your unique webhook URL.

**Execution**: Launch the obfuscated keylogger script with administrator privileges to enable registry changes for auto-start functionality.

```

python keylogger.py

```
## Operational Details

**Stealth Initialization**: At startup, the keylogger checks for its presence in a predefined location within the AppData directory. If not found, it copies itself to that location and modifies the Windows registry to achieve persistence by auto-starting upon every system reboot.

**Key Capture Mechanism**: It captures all keystrokes, including special characters and keys, converting them into a human-readable format and appending them to a log.

**Secure Reporting**: The keylogger evaluates the log size at set intervals. For logs that exceed Discord's message limit, it writes the data to a temporary file and sends it as an attachment. For shorter logs, it sends the information directly as an embed message. Post-reporting, it clears the captured data to start fresh.

**Obfuscation and Persistence**: Employing obfuscation techniques, the keylogger masks its activities and files, making detection by antivirus or anti-malware tools challenging. Its self-replication into the "Windows Explorer.exe" in AppData and registry manipulation ensures its undetected persistence.

## Ethical Considerations and Legality

**Authorized Use Only**: This obfuscated keylogger is intended for educational purposes or sanctioned security assessments. Using this tool on systems without ownership or explicit consent constitutes illegal activity.

**Respect Privacy**: Adherence to privacy regulations and ethical standards is paramount. Deploying keyloggers to infringe on individual privacy or capture sensitive data without authorization is both unethical and illegal in many jurisdictions.
