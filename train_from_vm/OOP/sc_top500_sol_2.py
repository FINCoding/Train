from bs4 import BeautifulSoup
import requests

URL = 'https://www.codewars.com/users/leaderboard'

class Ladder():
  def __init__(self, position):
    self.position = position

class User():
  def __init__(self, name, clan, honor):
    self.name, self.clan, self.honor = name, clan, honor

def solution():
  soup = BeautifulSoup(requests.get(URL).text, 'html.parser')
  users = dict()
  for i, user_item in enumerate(soup.find_all('tr')[1:], 1):
    users[i] = User(
      user_item['data-username'],
      user_item.find_all('td')[-2].text,
      int(user_item.find_all('td')[-1].text.replace(',', ''))
    )
  return Ladder(users)