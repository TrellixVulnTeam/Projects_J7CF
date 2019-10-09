import sys
import difflib
from difflib import get_close_matches
from flaskwsite import edict_f


def main(word):
    while True:
        word = word.lower()
        if word == '/exit':
            break
        elif edict_f.translate(word):
            return (' \n '.join(edict_f.translate(word)))
        elif edict_f.similar_search(word):
            searched = edict_f.similar_search(word)
            return ('Did you mean?: {}'.format(searched))

        else:
            return ("Unknown word... Please try again.")
