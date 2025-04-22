from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):

    ytt_api = YouTubeTranscriptApi()

    video = ytt_api.fetch("pKuguDpmti4")

    transcript = ""

    for snippet in video.snippets:
        transcript += snippet.text

    return transcript.split()
