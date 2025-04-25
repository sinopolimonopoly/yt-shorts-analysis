from dotenv import load_dotenv
from collections import defaultdict

import requests
import os

load_dotenv()
api_key = os.getenv("API_KEY")

def get_video_ids(playlist_id,max_results):
    video_ids=[]
    next_page_token = None

    url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults={max_results}&playlistId={playlist_id}&key={api_key}"

    if next_page_token:
        url += f"&pagetoken={next_page_token}"

    res = requests.get(url).json()
    for item in res['items']:
        video_id = item['snippet']['resourceId']['videoId']
        video_ids.append(video_id)

    return video_ids

