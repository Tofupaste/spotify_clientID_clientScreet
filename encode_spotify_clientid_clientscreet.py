import base64

client_id = "Your Client ID"
client_secret = "Your Client Secret"
credentials = f"{client_id}:{client_secret}"
encoded_credentials = base64.b64encode(credentials.encode()).decode()
print(encoded_credentials)