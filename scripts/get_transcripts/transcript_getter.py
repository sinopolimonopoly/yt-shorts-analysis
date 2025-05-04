from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):

    ytt_api = YouTubeTranscriptApi()

    video = ytt_api.fetch(video_id)

    transcript = []
    trans_table = str.maketrans('', '', ".,")

    for snippet in video.snippets:
        for word in snippet.text.split():
            word_no_punctuation = word.translate(trans_table)
            transcript.append(word_no_punctuation.lower())

    return transcript
