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


def top_5_words_algo(gen_sen, ignore=None | str) -> dict[str, int]:
    ignore_words = [*STOP_WORDS]
    if ignore:
        ignore_words.extend((j.strip() for j in ignore.lower().split(',')))
    textIO = StringIO()
    f = open('./temp/raw.txt', 'w')
    fs = open('./temp/sep.txt', 'w')
    for sen in gen_sen:
        textIO.write(sen.lower())
        textIO.write(" ")
        f.write(sen.lower())
        f.write(" ")
    t = textIO.getvalue()
    for s in t.split():
        k = s.strip()
        w = k if k not in ignore_words else f"DELETED {k}"
        fs.write(w)
        fs.write('\n')
    gen = (i for i in t.split() if i not in ignore_words)
    return Counter(gen).most_common(5)