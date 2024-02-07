import requests
from bs4 import BeautifulSoup
import time

url = "https://chat.openai.com/c/b5ed7c28-881a-4952-ad79-b5ec244804cd"

try:
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract user data based on a more flexible approach
        user_data = []
        for user_element in soup.find_all('div', class_='user-info'):
            username = user_element.find('span', class_='username')
            email = user_element.find('span', class_='email')

            if username and email:
                user_data.append({'username': username.text, 'email': email.text})

        print(f"User data: {user_data}")

    else:
        print(f"Failed to retrieve user data. Status Code: {response.status_code}")

except requests.RequestException as e:
    print(f"Error during request: {e}")

# Introduce a delay to avoid rate limiting
time.sleep(1)  # Adjust the delay as needed
