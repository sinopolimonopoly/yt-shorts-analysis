from transcript_getter import get_transcript
from phrase_checker import check_for_phrase

phrase = "smoking over applewood low and slow"

transcript = get_transcript("OU4S0FSZkoI")
print(transcript)

phrase_count = check_for_phrase(phrase.split(), transcript)
print(phrase_count)