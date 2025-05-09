from collections import Counter

def count_words(transcript):
    count = Counter(transcript)
    print(count)
    return count
