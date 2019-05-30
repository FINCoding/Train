import requests
import re

from bs4 import BeautifulSoup

URL = 'https://www.codewars.com/users/leaderboard'

def solution():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html')
    lst_tag = soup.find_all(has_class_username)
    top500 = leaderboard()
    for tag in lst_tag:
        name = tag['data-username']
        tag_childs = tag.find_all(get_clan_honor)
        clan = tag_childs[0].string
        if clan == None: clan = ''
        honor = tag_childs[1].string
        honor = int(honor.replace(',', ''))
        top500.position.append(user(name, clan, honor))
    print(len(top500.position))

class leaderboard:
    def __init__(self):
        self.position = position()

class position(list):
    def __getitem__(self, item):
        return super(position, self).__getitem__(item - 1)

    # def append(self,value):
    #     self.position_list.append(value)


    def __getitem__(self, key):
        return self.position_list[key-1]


def get_clan_honor(tag):
    return tag.name == 'td' and not tag.has_attr('class')

def has_class_username(tag):
    return tag.has_attr('data-username')

class user:
    def __init__(self,name,clan,honor):
        self.name = name
        self.clan = clan
        self.honor = honor

# class cust_lst(list):
#     def __getitem__(self, item):
#         return super(cust_lst,self).__getitem__(item-1)

if __name__ == '__main__':
    a = solution()
    # a = cust_lst()
    # a.append('a')
    # a.append('b')
    # print(len(a))
    # # print(a[0])
    # print(a[2])
    # b = []
    # b.append('a')
    # b.append('b')
    # print(b[-1])



