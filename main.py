import requests
import time
import smtplib
import os

# The URL of the website you want to monitor
url = 'https://www.gseb.org'

# The file name where the previous version of the website data was saved
previous_data_file = 'previous_data.txt'

if not os.path.exists(previous_data_file):
    with open(file_path, 'w') as f:
        f.write('Initial content')

def notify():
    # Replace YOUR_TOKEN with your actual bot token and YOUR_CHAT_ID with your actual chat ID
    BOT_TOKEN = 'YOUR_TOKEN'
    CHAT_ID = 'YOUR_CHAT_ID'

    # Define the message you want to send
    message = 'Site Updated (gseb.org)!'

    # Send the message to the Telegram channel using the Telegram Bot API
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}'
    response = requests.get(url)

    # Check if the message was sent successfully
    if response.status_code == 200:
        print('Message sent successfully')
    else:
        print(f'Error sending message: {response.content}')

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

