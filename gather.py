from bs4 import BeautifulSoup
from requests import get

search_word = None
def gather():
    global search_word
    words = list()
    search_word = input('> ')
    # Weblio
    url = 'https://thesaurus.weblio.jp/content/' + search_word
    response = get(url)
    # print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    td1 = soup.find_all('td', class_='nwntsR')
    td2 = soup.find_all('td', class_='wrugjR')
    for t in td1:
        for a in t.find_all('a', class_='crosslink'):
            # print(a.text)
            words.append(a.text)
    for t in td2:
        for a in t.find_all('a', class_='crosslink'):
            # print(a.text)
            words.append(a.text)
    # 日本語シソーラス
    url = 'https://renso-ruigo.com/word/' + search_word
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    td = soup.find('div', class_='word_t_field')
    # print(td.find_all('a'))
    for t in td.find_all('a'):
        print(t.text)
        words.append(t.text)
    return words
