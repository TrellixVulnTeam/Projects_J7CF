import json
import difflib
from difflib import  get_close_matches

datajson = json.load(open('data.json'))

def translate(w):

    if w in datajson:
        return datajson[w]
    elif w.title() in datajson:
        return datajson[w.title()]
    elif w.upper() in datajson:
        return datajson[w.upper()]
    else:
        return 0

def similar_search(w):

    return str(''.join(get_close_matches(w, datajson, 1)))

