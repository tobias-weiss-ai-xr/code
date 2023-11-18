#!/usr/bin/python3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Establish SMTP Connection
s = smtplib.SMTP_SSL('www.tobias-weiss.org', 465)

# Login Using Your Email ID & Password
s.login("c@tobias-weiss.org", "")

msg = MIMEMultipart()

# Setting Email Parameters
msg['From'] = "<tobias@tobias-weiss.org>"
msg['To'] = "<tobias@tobias-weiss.org>"
msg['Subject'] = "SENT BY ME"

# Email Body Content
message = """
Hello, this is a test message!
"""

# Add Message To Email Body
msg.attach(MIMEText(message, 'text'))

# To Send the Email
s.send_message(msg)

# Terminating the SMTP Session
s.quit()

