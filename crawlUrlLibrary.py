import requests
from bs4 import BeautifulSoup


class CrawlCinema:
    def __init__(self):
        print('running')

    def trade_spider(self):
        url = 'https://www.qfxcinemas.com'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        soup_all_qfx_div_tags = soup.findAll('div', {'class': 'movie'})
        movie = {}
        for i in soup_all_qfx_div_tags:
            movie_name = i.find('h4').text
            a_tag_ticket_class = i.findAll('a', {'class': 'ticket'})
            if len(a_tag_ticket_class)>0:
                movie[movie_name] = True
            else:
                movie[movie_name] = False
        return movie
