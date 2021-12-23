from urllib import request

from bs4 import BeautifulSoup


def parse_title(url):
    soup = BeautifulSoup(send_request_get_html_page(url), 'html.parser')
    return soup.title.text


def send_request_get_html_page(url):
    req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'})
    return request.urlopen(req).read()
