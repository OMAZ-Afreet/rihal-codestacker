from io import StringIO
import re
import string
from collections import Counter


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


def top_5_words_algo(gen_sen, ignore_num) -> dict[str, int]:
    textIO = StringIO()
    for sen in gen_sen:
        textIO.write()
    
    