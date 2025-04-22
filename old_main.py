from download_video import download_video
from extract_audio import extract_audio
from speech_to_text import transcribe_audio
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

        url = row[0]
        print("Downloading video...")
        video_path = download_video(url, output_path="data/videos/")

        print("Extracting audio...")
        audio_path = extract_audio(video_path, output_audio_path="data/audio/")

        print("Transcribing audio...")
        transcript = transcribe_audio(audio_path, output_transcript_path="data/transcripts/")
        transcript_list = transcript.split()

        print("Transcript completed")

        phrase_count = check_for_phrase(phrase.split(), transcript_list)

        print(f'Video {bruh} | Phrase Count: {phrase_count}')

        end = time.time()
        print(f'Time taken: {end-start}\n')
        bruh += 1

        if bruh > 4: break



"""
start = time.time()

url = input("Enter your YouTube Short URL here: ")
print("Downloading video...")
video_path = download_video(url, output_path="data/videos/")

print("Extracting audio...")
audio_path = extract_audio(video_path, output_audio_path="data/audio/")

print("Transcribing audio...")
transcript = transcribe_audio(audio_path, output_transcript_path="data/transcripts/")
transcript_list = transcript.split()

print("\nTranscript:\n", transcript)



end = time.time()
print(f'Time taken: {end-start}')

"""