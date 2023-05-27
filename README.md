# InstaBot
Make sure to replace 'your_username' and 'your_password' with your actual Instagram credentials. The script first sends a GET request to the login page to extract the CSRF token required for authentication. Then, it sends a POST request to the login API endpoint with the username, password, and CSRF token to log in. If the login is successful, it prints "Login successful!" and demonstrates an additional action by retrieving the user's profile page. If the login fails, it prints "Login failed!".

Note that using automated scripts to log into Instagram may violate their terms of service, and they may have measures in place to prevent automated logins. It's always recommended to check the terms and conditions of the platform before creating automated scripts.
