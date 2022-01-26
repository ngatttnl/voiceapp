import requests

url = 'https://api.fpt.ai/hmi/tts/v5'

payload = 'con mèo'
headers = {
    'api-key': 'Et5Nt5RHrE0z61EkYLI9jzgfTY8QFw7u',
    'speed': '',
    'voice': 'linhsan'
}
def app():
    response = requests.request('POST', url, data=payload.encode('utf-8'), headers=headers)
    print(response.text)