from nltk import FreqDist
import string
import re
from pymystem3 import Mystem

extended_punctuation = string.punctuation + '—»«...'
def passed_filter (some_word, stoplist):
    some_word = some_word.strip()
    if some_word in extended_punctuation:
        return False
    elif some_word in stoplist:
        return False
    elif re.search ('[А-ЯЁа-яёA-Za-z]', some_word) == None:
        return False
    return True

moi_analizator = Mystem()
def keywords_most_frequent_with_stop_and_lemm (some_text, num_most_freq, stoplist):    
    lemmatized_text = [word for word in moi_analizator.lemmatize(some_text.lower()) 
                    if passed_filter(word, stoplist)]
    return [word_freq_pair[0] for word_freq_pair in FreqDist(lemmatized_text).most_common(num_most_freq)]