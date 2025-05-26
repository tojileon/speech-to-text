import requests
from config import API_KEY

# Speech to Text (POST /speech-to-text)
response = requests.post(
  "https://api.sarvam.ai/speech-to-text",
  headers={
    "api-subscription-key": API_KEY
  },
  data={
    'language_code': "ml-IN",
    'model': "saarika:v2",
  },
  files={
    'file': ('test1.wav', open('test1.wav', 'rb')),
  },
)

print(response.json())