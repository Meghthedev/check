import requests
import time
import smtplib

# The URL of the website you want to monitor
url = 'https://www.gseb.org'

# The file name where the previous version of the website data was saved
previous_data_file = 'previous_data.txt'

while True:
    # Retrieve the current website data
    response = requests.get(url, verify=False)
    current_data = response.text

    # Compare the current data with the previous data
    with open(previous_data_file, 'r') as f:
        previous_data = f.read()

    if current_data != previous_data:
        # The website has been updated, so send a notification
        print('Website updated!')
        notify()
        
    # Save the current website data for future comparison
    with open(previous_data_file, 'w') as f:
        f.write(current_data)

    # Wait for a certain amount of time before checking again
    time.sleep(300) # Check every 5 minutes

def notify():
    # Send a notification using your preferred method, such as email or push notification
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"
        
    # The recipient's email address
    recipient_email = "recipient_email@example.com"

    # The subject and body of the email
    subject = "Website update"
    body = "The website has been updated!"

    # Connect to the Gmail SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
    smtp_connection.starttls()
    smtp_connection.login(sender_email, sender_password)

    # Create the email message
    message = f"Subject: {subject}\n\n{body}"

    # Send the email
    smtp_connection.sendmail(sender_email, recipient_email, message)

    # Close the SMTP connection
    smtp_connection.quit()