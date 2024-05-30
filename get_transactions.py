import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv('API_BASE_URL')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

auth_str = f"{CLIENT_ID}:{CLIENT_SECRET}"
auth_bytes = auth_str.encode('ascii')
auth_base64 = base64.b64encode(auth_bytes).decode('ascii')

##Building authentication in Base64 encoding
headers = {
    'Authorization': f'Basic {auth_base64}',
    'Content-Type': 'application/json'
}

# Voorbeeld endpoint en data
endpoint = f"{API_BASE_URL}/TransactionRecords"
data = {
    # Optional data to post
}

response = requests.post(endpoint, headers=headers, json=data)

if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Error:", response.status_code, response.text)