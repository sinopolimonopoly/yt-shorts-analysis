from dotenv import load_dotenv

import requests
import os

load_dotenv()
api_key = os.getenv("API_KEY")

def get_channel_id(handle):

    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&type=channel&q={handle}&key={api_key}"

    res = requests.get(url).json()
    print(res)
    channel_id = res['items'][0]['snippet']['channelId']
    print("Channel ID:", channel_id,"\n")
    return channel_id
