from django.core.paginator import Paginator


def paginate(q, req):
    try:
        n = int(req.data['paginate'])
        p = int(req.data.get('page', 1))
        paginator = Paginator(q, n) 
        return paginator.get_page(p), paginator.num_pages
    except:
        return False