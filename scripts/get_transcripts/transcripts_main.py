import sys
import os

from transcript_getter import get_transcript
from phrase_checker import check_for_phrase

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from output.phrase_counts.console_outputter import output_dict
from output.phrase_counts.csv_maker import create_phrase_csv

from collections import defaultdict
import csv
import time

start = time.time()

# Channel name
channel = "maxthemeatguy"

# Phrases, words to count for
phrase = "smoking over applewood low and slow"
sub_phrase = "low and slow"
word = "applewood"

# Dictionary to store data
phrase_dict = defaultdict(dict)

# CSV file to read video IDs from 
csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data/video_lists/maxthemeatguy_shorts_list.csv'))
vid_data = open(csv_path, encoding='utf8')
reader = csv.reader(vid_data)

# Skip header row
next(reader)
counter = 0

print(f'{'ID':<13} {'Video':<60} {'SOALAS Count':<20} {'LAS Count':<20} {'Applewood Count':<20} {'Transcript?':<12}')

# Outputting rows one at time instead of all at once because this takes a minute
for row in reader:
    counter += 1
    video_id = row[0]

    transcript = get_transcript(video_id)

    video_title = row[1]
    phrase_count = check_for_phrase(phrase.split(), transcript)
    sub_phrase_count = check_for_phrase(sub_phrase.split(), transcript)
    word_count = transcript.count(word)
    is_transcript = "Yes" if (len(transcript) > 0) else "No"

    phrase_dict[video_id]["Title"] = video_title
    phrase_dict[video_id]["SOALAS Count"] = phrase_count
    phrase_dict[video_id]["LAS Count"] = sub_phrase_count
    phrase_dict[video_id]["Applewood Count"] = word_count
    phrase_dict[video_id]["Transcript?"] = is_transcript

    print(f'{video_id:<13} {video_title:<60} {phrase_count:<20} {sub_phrase_count:<20} {word_count:<20} {is_transcript:<12}')

# output_dict(phrase_dict)

end = time.time()
print(f"Time Taken: {end-start}")

create_phrase_csv(phrase_dict, channel)
