from transcript_getter import get_transcript
from phrase_checker import check_for_phrase

import csv

phrase = "smoking over applewood low and slow"
word = "applewood"

vid_data = open('../data/video_lists/maxthemeatguy_shorts_list.csv', encoding='utf8')

reader = csv.reader(vid_data)

# Skip header row
next(reader)
counter = 0

print(f'{'Video':<60} {'SOALAS Count':<20} {'Applewood Count':<20}')

for row in reader:
    counter += 1
    video_id = row[0]
    video_title = row[1]

    transcript = get_transcript(video_id)
    #print(transcript)

    phrase_count = check_for_phrase(phrase.split(), transcript)
    word_count = transcript.count(word) 

    print(f'{video_title:<60} {phrase_count:<18} {word_count:<20}')

    if counter > 2: break