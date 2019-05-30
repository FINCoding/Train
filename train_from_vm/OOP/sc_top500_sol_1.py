from urllib.request import urlopen
from bs4 import BeautifulSoup


class User:
    def __init__(self, name, honor, clan=''):
        self.name = name
        self.honor = honor
        self.clan = clan


class LeaderBoard:
    def __init__(self, url):
        self.url = url
        self.position = {}

    def fill_position(self):
        page = urlopen(self.url)
        soup = BeautifulSoup(page, 'html.parser')
        trs = soup.find('div', class_='leaderboard').find('table').find_all('tr')
        for tr in trs:
            if tr.has_attr('data-username'):
                clan = tr.contents[2].string if tr.contents[2].string else ''
                user = User(tr['data-username'], int(tr.contents[3].string.replace(',', '')), clan)
                position = int(tr.contents[0].string[1:])
                self.position[position] = user


URL = 'https://www.codewars.com/users/leaderboard'


def solution():
    board = LeaderBoard(URL)
    board.fill_position()
    return board