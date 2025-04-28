import csv
import requests
from collections import defaultdict

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
counter = 0


with open('manual_list.csv') as shorts_list:
    reader = csv.reader(shorts_list)

    list_dict = defaultdict(str)

    list_lists = list(reader)

    ids_list = [list_lists[i][0] for i in range(0, len(list_lists))]

    for i in range(0, len(ids_list), 50):
        batch = ids_list[i : i+50]

        url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={','.join(batch)}&key={api_key}"
        res = requests.get(url).json()

        for item in res['items']:
            vid_id = item['id']
            title = item['snippet']['title']

            list_dict[vid_id] = title

print(list_dict)

with open('manual_w_titles.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)

    writer.writerow(["Video ID", "Video Title"])

    for id, title in list_dict.items():
        writer.writerow([id, title])


    