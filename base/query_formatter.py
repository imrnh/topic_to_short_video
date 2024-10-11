BASE_URL = "https://scholar.google.com/scholar?as_ylo=2020&q="
URL_TAIL = "&hl=en&as_sdt=0,5"

def build_search_url(search_query):
    qlist = search_query.split(" ")
    search_query = ("+").join(qlist)

    return BASE_URL + search_query + URL_TAIL