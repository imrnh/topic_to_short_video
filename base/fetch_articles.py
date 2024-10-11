import os
import requests
from bs4 import BeautifulSoup

# Filter functions. Only consider urls with pdf file. And file url starts with http or https. Other js and css resources have urls too which the code otherwise would load if not filtered.
valid_url = lambda url:  url.startswith(('http://', 'https://'))
have_pdf_file = lambda text:  text.__contains__("PDF")

def fetch_article_url(url):
    try:
        response = requests.get(url, headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        })

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser') # Parse the HTML content using BeautifulSoup
            a_tags = soup.find_all('a')  # Find all <a> tags (hyperlinks)

            content_list = []
            for tag in a_tags:
                _href = tag.get('href')
                _text = tag.get_text()

                if valid_url(_href) and have_pdf_file(_text):
                    content_list.append({"url": _href, "text": _text})

            return content_list
        
        else: 
            print(f"Failed to get webpage = {url} with status code: {response.status_code}")

    except Exception as e:
        print(f"Exception at `fetch_article_url`: {e}")



def download_article(url, file_name):
    """
        Download a PDF file from a given URL and save it locally.
        
        :param url: URL of the PDF to download
        :param file_name: index of the pdf file.
        :return: Path to the downloaded PDF file
    """
    try:
        os.makedirs("pdf", exist_ok=True)
        response = requests.get(url)
        if response.status_code == 200:
            full_path = f"pdf/{file_name}.pdf"
            with open(full_path, 'wb') as pdf_file:
                pdf_file.write(response.content)
            return full_path
        else:
            return None
        
    except Exception as e:
        print(f"Exception at `download_article`: {e}")