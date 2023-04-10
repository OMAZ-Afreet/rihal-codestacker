from django.contrib.postgres.search import SearchQuery, SearchVector
from .models import PDFSearch

ADVANCE_SEARCH_MODES = ('c', 'ic', 'e', 'ie', 'sw', 'isw', 'ew', 'iew', 'ph', 'eng',  'def')
SV = SearchVector("sentence")


def match_search(prompt: str):
    # mode, search = None, None
    try:
        mode, s = prompt.split(":")
    except:
        return False, '', {"error": f"invalid advance search format. MUST BE: [mode]:[search]. Available modes: {ADVANCE_SEARCH_MODES}"}
    
    m = PDFSearch.objects
    res = None
    match mode.lower():
        case 'c':
            res = m.filter(sentence__contains=s)
        case 'ic':
            res = m.filter(sentence__icontains=s)
        case 'e':
            res = m.filter(sentence__exact=s)
        case 'ie':
            res = m.filter(sentence__iexact=s)
        case 'sw':
            res = m.filter(sentence__startswith=s)
        case 'isw':
            res = m.filter(sentence__istartswith=s)
        case 'ew':
            res = m.filter(sentence__endswith=s)
        case 'iew':
            res = m.filter(sentence__iendswith=s)
        case 'ph':
            res = m.annotate(search=SV).filter(search=SearchQuery(s, search_type="phrase"))
        # case 'raw':
        #     res = m.annotate(search=SV).filter(search=SearchQuery(s, search_type="raw"))
        case 'eng':
            res = m.annotate(search=SV).filter(search=SearchQuery(s, config="english"))
        case _:
            res = m.filter(sentence__search=s)
            mode = 'def'
    
    return True, mode, res