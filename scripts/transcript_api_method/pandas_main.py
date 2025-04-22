from title_getter import get_title
from transcript_getter import get_transcript
from phrase_checker import check_for_phrase

import pandas as pd
import time

phrase = "smoking over applewood low and slow"

urls = pd.read_csv('../../data/mtmg_shorts.csv')
