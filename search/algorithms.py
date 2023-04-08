from io import StringIO
import re
# import string
from collections import Counter

from .stop_words import STOP_WORDS

def count_word_algo(word: str, sentences: list[str]) -> int:
    #* Old *#
    # count = 0
    # for sentence in sentences:
    #     for w in sentence.split():
    #         if word.lower() == w.lower().translate(str.maketrans("", "", string.punctuation)):
    #             count+=1
    # return count
    # WORD_RE = re.compile(, )
    textIO = StringIO()
    for s in sentences:
        textIO.write(s)
        textIO.write(" ")
    l =  re.findall(fr'\b{word}\b', textIO.getvalue(), re.IGNORECASE)
    return len(l)

WORDS = re.compile(r'\b\w+\b')
def top_5_words_algo(gen_sen, ignore=None | str, top=None | str) -> dict[str, int]:
    ignore_words = {*STOP_WORDS}
    _top = 5
    if ignore:
        ignore_words.update((j.strip() for j in ignore.lower().split(',')))
    
    if top:
        try:
            _top = int(top)
        except:
            pass
    
    # print(ignore_words)
    textIO = StringIO()
    # f = open('./temp/raw.txt', 'w')
    # fs = open('./temp/sep.txt', 'w')
    for sen in gen_sen:
        textIO.write(sen.lower())
        textIO.write(" ")
        # f.write(sen.lower())
        # f.write(" ")
    t =  re.findall(r'\b\w+\b', textIO.getvalue())
    # for s in t:
    #     w = s if s not in ignore_words else f"DELETED {s}"
    #     fs.write(w)
    #     fs.write('\n')
    gen = (i for i in t if i not in ignore_words and len(i) > 2)
    return Counter(gen).most_common(_top)