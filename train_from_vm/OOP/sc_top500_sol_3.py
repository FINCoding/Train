import requests
from bs4 import BeautifulSoup


URL = 'https://www.codewars.com/users/leaderboard'



def solution():
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'html.parser')
    z = soup.findAll('tr')[1:]
    man = {}
    for x in z:
        place = int(x.find(attrs={'class': 'rank is-small'}).string[1:])
        user_name = x.find('a')['href'][7:]
        user_clan = '' if x.findAll('td')[2].string is None else x.findAll('td')[2].string
        user_honor = x.findAll('td')[3].string
        man.update({place: User(place, user_name.replace('%20', ' '), user_clan, int(user_honor.replace(',', '')))})
    return Man(man)

class User:
    def __init__(self, place, user_name, user_clan, user_honor):
        self.place = place
        self.user_name = user_name
        self.user_clan = user_clan
        self.user_honor = user_honor
    @property
    def name(self):
        return self.user_name

    @property
    def clan(self):
        return self.user_clan

    @property
    def honor(self):
        return self.user_honor

class Man:
    def __init__(self, pl):
        self.pl = pl

    @property
    def position(self):
        return self.pl