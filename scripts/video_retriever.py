import requests
import re

from collections import defaultdict

API_KEY = "censored"

videos = defaultdict(dict)

def get_channel_id(handle):

    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&type=channel&q={handle}&key={API_KEY}"

    res = requests.get(url).json()
    print(res)
    channel_id = res['items'][0]['snippet']['channelId']
    print("Channel ID:", channel_id)
    return channel_id

def get_uploads_playlist_id(channel_id):
    url = f"https://www.googleapis.com/youtube/v3/channels?part=contentDetails&id={channel_id}&key={API_KEY}"
    res = requests.get(url).json()
    playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    return playlist_id

def get_all_videos(playlist_id):
    video_ids = []
    next_page_token = None

    counter = 0

    while True:
        url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=5&playlistId={playlist_id}&key={API_KEY}"

        if next_page_token:
            url += f"&pagetoken={next_page_token}"

        res = requests.get(url).json()
        for item in res['items']:
            print(item['snippet']['resourceId'])
            video_id = item['snippet']['resourceId']['videoId']
            title = item['snippet']['title']
            upload_date = item['snippet']['publishedAt'][0:10]
            description = item['snippet']['description'][0:10]

            videos[video_id]["Title"] = title
            videos[video_id]["Upload Date"] = upload_date
            videos[video_id]["Description"] = description


        next_page_token = res.get('nextPageToken')

        if counter >= 0:
            break

        if not next_page_token:
            break

        counter += 1

def get_short_vids(video_ids):

    shorts = []

    for i in range(0, len(video_ids), 50):
        batch = video_ids[i:i+50]

        url = f"https://www.googleapis.com/youtube/v3/videos?part=contentDetails,snippet&id={','.join(batch)}&key={API_KEY}"
        res = requests.get(url).json()
        for video in res['items']:
            raw_duration = video['contentDetails']['duration']
            print(raw_duration, process_duration(raw_duration))
            duration = video['contentDetails']['duration']
            title = video['snippet']['title']
            match = re.match(r'PT(\d+)S', duration)

            if match and int(match.group(1)) <= 120:
                shorts.append({
                    'title': title,
                    'id': video['id'],
                    'url': f"https://www.youtube.com/watch?v={video['id']}"
                })

    print(shorts)
    return shorts

def process_duration(raw_duration):
    duration = raw_duration.replace("PT", "")

    if "M" in duration:
        minute_idx = duration.index("M")
        min_seconds = int(duration[0:minute_idx]) * 60
        leftover_seconds = int(duration[minute_idx+1:len(duration)-1])

        duration_in_s = min_seconds + leftover_seconds

    else:
        duration_in_s = int(duration[0:-1])
    
    return duration

bruh = "maxthemeatguy"
id = get_channel_id(bruh)
uploads_id = get_uploads_playlist_id(id)


get_all_videos(uploads_id)

all_video_ids = [k for (k, v) in videos.items()]

print(all_video_ids)

get_short_vids(all_video_ids)