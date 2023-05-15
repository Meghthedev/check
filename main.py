import requests
import time

# The URL of the website you want to monitor
url = 'https://www.gseb.org'

# The file name where the previous version of the website data was saved
previous_data_file = 'previous_data.txt'

while True:
    # Retrieve the current website data
    response = requests.get(url)
    current_data = response.text

    # Compare the current data with the previous data
    with open(previous_data_file, 'r') as f:
        previous_data = f.read()

    if current_data != previous_data:
        # The website has been updated, so send a notification
        print('Website updated!')
        # Send a notification using your preferred method, such as email or push notification

    # Save the current website data for future comparison
    with open(previous_data_file, 'w') as f:
        f.write(current_data)

    # Wait for a certain amount of time before checking again
    time.sleep(300) # Check every 5 minutes
