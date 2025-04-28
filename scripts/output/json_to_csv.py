import json
import csv

from pathlib import Path

current_file = Path(__file__)

project_root = current_file.parents[2]

json_file = project_root / 'mtmg_vids.json'

with open(json_file, 'r') as file:
    videos = json.load(file)

with open('mtmg_videos.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)

    writer.writerow(["Video ID", "Title", "Upload Date", "Raw Duration", "Duration in S", "View Count", "Like Count", "Comment Count"])

    for video_id, info in videos.items():
        title = info.get("Information").get("Title")
        upload_date = info.get("Information").get("Upload Date")
        duration = info.get("Information").get("Duration").get("min_sec")
        duration_secs = info.get("Information").get("Duration").get("secs")
        view_count = info.get("Statistics").get("View Count")
        like_count = info.get("Statistics").get("Like Count")
        comment_count = info.get("Statistics").get("Comment Count")

        writer.writerow([video_id, title, upload_date, duration, duration_secs, view_count, like_count, comment_count])
