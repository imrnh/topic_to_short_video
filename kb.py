from tqdm.auto import tqdm 

from base.fetch_articles import fetch_article_url, download_article
from base.query_formatter import build_search_url
from base.pdf_ops import pdf_text_extractor
from base.filter_pdf_contents import filter_file_content

def make_knowledge_base(search_query, video_title):
    search_url = build_search_url(search_query)
    search_contents = fetch_article_url(search_url)

    knowledge_base = []

    for file_idx, search_content in tqdm(enumerate(search_contents[:2])):
        file_url = search_content['url']

        full_path = download_article(file_url, file_name=str(file_idx))

        if full_path != None:
            file_content = pdf_text_extractor(full_path)
            filtereted_content = filter_file_content(file_content, video_title)
            
            knowledge_base.append(filtereted_content)

    return knowledge_base