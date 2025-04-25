from dotenv import load_dotenv
from collections import defaultdict

import requests
import os

load_dotenv()
api_key = os.getenv("API_KEY")

def get_videos(playlist_id, max_results, max_duration=False):
    videos = defaultdict(dict)
    next_page_token = None

    counter = 0

    while True:
        url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults={max_results}&playlistId={playlist_id}&key={api_key}"

        if next_page_token:
            url += f"&pagetoken={next_page_token}"

        res = requests.get(url).json()
        for item in res['items']:
            print(item)
            raw_duration = item['snippet']['contentDetails']['duration'].replace("PT", "")

            if max_duration == True:
                processed_duration = process_duration(raw_duration)

                if processed_duration > max_duration:
                    continue
            

            # Get video information
            video_id = item['snippet']['resourceId']['videoId']
            title = item['snippet']['title']
            upload_date = item['snippet']['publishedAt'][0:10]

            videos[video_id]["Title"] = title
            videos[video_id]["Upload Date"] = upload_date
            
            if max_duration == True:
                videos[video_id]["Duration"] = {"min_sec": raw_duration, "secs" : processed_duration}

            else:
                videos[video_id]["Duration"] = raw_duration

        next_page_token = res.get('nextPageToken')

        if not next_page_token:
            break

        counter += 1

