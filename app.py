import requests

# Set up the payload with the user's current and new passwords
payload = {
    'passwordOld': 'CURRENT_PASSWORD',
    'passwordNew': 'NEW_PASSWORD',
    'passwordNewConfirm': 'NEW_PASSWORD'
}

# Send the POST request to the password reset endpoint
response = requests.post('https://www.roblox.com/account/settings/security/password', data=payload)

# Check the response status code to see if the password was successfully changed
if response.status_code == 200:
    print("Password successfully changed!")
else:
    print("Error: Password not changed. Response code:", response.status_code)
