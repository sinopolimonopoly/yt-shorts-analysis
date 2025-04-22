import time


def check_for_phrase(phrase, transcript):

    phrase_present = False
    current_phrase = []
    current_idx = 0

    phrase_counter = 0

    for word in transcript:
        if word.lower() == phrase[current_idx]:
            phrase_present = True
            current_phrase.append(word.lower())
            current_idx += 1

            if current_phrase == phrase:
                phrase_counter += 1
                
                phrase_present = False
                current_phrase = []
                current_idx = 0


        else:
            phrase_present = False
            current_phrase = []
            current_idx = 0


    return phrase_counter

        