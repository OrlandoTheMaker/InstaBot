import requests
from bs4 import BeautifulSoup

LOGIN_URL = 'https://www.instagram.com/accounts/login/'
LOGIN_API_URL = 'https://www.instagram.com/accounts/login/ajax/'

USERNAME = 'your_username'
PASSWORD = 'your_password'


def login(username, password):
    # Create a session
    session = requests.Session()

    # Get the login page HTML to extract the CSRF token
    response = session.get(LOGIN_URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'}).get('value')

    # Prepare the login data
    login_data = {
        'username': username,
        'password': password,
        'csrfmiddlewaretoken': csrf_token
    }

    # Send the login request
    headers = {
        'Referer': LOGIN_URL,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/58.0.3029.110 Safari/537.3',
        'X-Requested-With': 'XMLHttpRequest'
    }
    login_response = session.post(LOGIN_API_URL, data=login_data, headers=headers)
    login_json = login_response.json()

    if 'authenticated' in login_json and login_json['authenticated']:
        print('Login successful!')
        # You are now logged in and can perform further actions using the session object
        # For example, you can retrieve the user's profile page
        profile_response = session.get(f'https://www.instagram.com/{username}/')
        print(profile_response.text)
    else:
        print('Login failed!')


# Call the login function with your Instagram credentials
login(USERNAME, PASSWORD)
