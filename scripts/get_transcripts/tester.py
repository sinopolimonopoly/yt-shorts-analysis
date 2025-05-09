from transcript_getter import get_transcript
from phrase_checker import check_for_phrase
from word_counter import count_words

phrase = "smoking over applewood low and slow"

transcript = get_transcript("D_QYRTqhtoQ")
print(transcript)

transcript_2 = get_transcript("KflDSgz4KIc")

phrase_count = check_for_phrase(phrase.split(), transcript)
print(phrase_count)

word_count = count_words(transcript)
print(word_count)

word_count.update(transcript_2)
print(word_count)