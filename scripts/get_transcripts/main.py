from title_getter import get_title
from transcript_getter import get_transcript
from phrase_checker import check_for_phrase

import csv 

import time

phrase = "smoking over applewood low and slow"

with open("mtmg_shorts.csv", mode="r") as url_list:
    url_csv = csv.reader(url_list)

    next(url_csv, None)

    bruh = 0
    for row in url_csv:
        start = time.time()

        # Video link and id
        video_url = row[0]
        video_id = video_url.replace("https://www.youtube.com/watch?v=", "")

        # Get video title
        title = get_title(video_url)

        # Get video transcript
        transcript_list = get_transcript(video_id)

        phrase_count = check_for_phrase(phrase.split(), transcript_list)

        print(f'Video: {title} | SOALAS Count: {phrase_count}')
        end = time.time()
        print(f'Time taken: {end-start}\n')
        bruh += 1

        if bruh > 1: break
