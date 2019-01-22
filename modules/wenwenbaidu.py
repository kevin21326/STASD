import requests
from bs4 import BeautifulSoup 

def get_keywords()
    url = 'https://baike.baidu.com/item/%E4%BF%AE%E7%9C%9F%E8%81%8A%E5%A4%A9%E7%BE%A4/18768294'
    
    s = requests.Session()
    s.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    # Ref: Browse the following links 
    # for the solution to "TooManyRedirects: Exceeded 30 redirects" exception
    # https://stackoverflow.com/questions/23651947/python-requests-requests-exceptions-toomanyredirects-exceeded-30-redirects 
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent
    
    page = s.get(url)
    soup = BeautifulSoup(page.text)
    
    keywords = []
    keywords += [a.text for a in soup.find_all('a')]
    keywords += [b.text for b in soup.find_all('b')]

    return keywords
