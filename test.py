from openai import OpenAI
import requests

try:
    response = requests.get(
                    "http://localhost:8880/v1/audio/voices"
                )
    print(response.text)
    response.raise_for_status()
    data = response.json()
    voices_list = data.get("voices", [])
    available_voices = {voice["id"]: voice["name"] for voice in voices_list}
    print(available_voices)
except Exception as e:
    print(e)