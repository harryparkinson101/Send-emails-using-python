import smtplib

# Set up the server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

# Log in to the server
server.login('your_email_address@gmail.com', 'your_password')

# Send the email
msg = 'Hello, this is a test email'
server.sendmail('your_email_address@gmail.com', 'recipient_email_address@gmail.com', msg)

# Disconnect from the server
server.quit()