from download_video import download_video
from extract_audio import extract_audio
from speech_to_text import transcribe_audio
from phrase_checker import check_for_phrase

import time

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