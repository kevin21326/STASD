import requests
from bs4 import BeautifulSoup 

def get_keywords(url='https://baike.baidu.com/item/%E4%BF%AE%E7%9C%9F%E8%81%8A%E5%A4%A9%E7%BE%A4/18768294', page_encoding='iso-8859-1'):
    s = requests.Session()
    s.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    # Ref: Browse the following links 
    # for the solution to "TooManyRedirects: Exceeded 30 redirects" exception
    # https://stackoverflow.com/questions/23651947/python-requests-requests-exceptions-toomanyredirects-exceeded-30-redirects 
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent
    
    page = s.get(url)
    soup = BeautifulSoup(page.text.encode(page_encoding), features='lxml')
    main_content = soup.find('div', {'class':'main-content'})
    stopwords = ['', ' ',',', ';', '：', '【', '】','\n', '\n\n', '\xa0', '\xa0\xa0', '\u3000',  '\u3000\u3000'] 

    keywords = []
    keywords += [a.text for a in main_content.find_all('a') if a.text not in stopwords]
    keywords += [b.text for b in main_content.find_all('b') if b.text not in stopwords]

    return keywords
