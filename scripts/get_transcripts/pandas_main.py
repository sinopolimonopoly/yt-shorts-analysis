from title_getter import get_title
from transcript_getter import get_transcript
from phrase_checker import check_for_phrase

import pandas as pd
import time

phrase = "smoking over applewood low and slow"

urls = pd.read_csv('../../data/mtmg_shorts.csv', header=0, names=['URL'])

counter = 0

for index, url in urls['URL'].items():
    print(counter)
    start = time.time()

    print(url)

    # Video link and id
    video_url = url
    video_id = video_url.replace("https://www.youtube.com/watch?v=", "")

    # Get video title
    title = get_title(video_url)

    # Get video transcript
    transcript_list = get_transcript(video_id)

    # Count phrase occurences
    phrase_count = check_for_phrase(phrase.split(), transcript_list)

    print(f'Video: {title} | SOALAS Count: {phrase_count}')
    end = time.time()
    print(f'Time taken: {end-start}\n')
    counter += 1

    if counter > 15: break

