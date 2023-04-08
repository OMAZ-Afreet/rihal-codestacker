import json 

from pdf_search.redis_db import r

# from .utils import bench

MONTH = 60 * 60 * 24 * 30


def check_top5_cache(id: int, words: str|None, top: str|None) -> tuple[bool, dict|None]:
    try:
        result = r.get(f"{id}:{words}:{top}")
        return result is not None, result
    except:
        False, None



def set_top5_cache(id: int, words: str|None, top: str|None, result: dict) -> tuple[bool, dict|None]:
    try:
        r.set(f"{id}:{words}:{top}", json.dumps(result), MONTH)
    except:
        return