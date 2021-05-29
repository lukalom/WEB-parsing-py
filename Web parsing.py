import csv
from bs4 import BeautifulSoup
import requests
import random
import time
p = {'page':1}
while p['page'] < 4:

    url = 'https://www.y8.com'

    r = requests.get(url, params=p)

    content = r.text

    soup = BeautifulSoup(content, 'html.parser')

    container = soup.find('div', id='items_container')
    items_in_container = container.find_all('div', {'class': 'item'})

    #parsing
    # print(items_in_container[0].find('div'))
    # technology = items_in_container[0].find_all('a')[1].find('div', {'class': 'technology'}).text.strip().replace('\n', '')
    # rating = items_in_container[0].find_all('a')[1].find('p', {'class': 'rating'}).text.strip().replace('\n', '')
    # plays_count = items_in_container[0].find_all('a')[1].find('p', {'class': 'plays-count'}).text.strip().replace('\n', '')


    #printing game name engine popularity
    # print(items_in_container[0].text.strip())
    # x = items_in_container[0].text.strip()
    # a = x.replace('\n', " ")
    # print(a.split())
    f = open('info.csv', 'w', encoding='utf-8_sig')
    f.write('Name' + ',' + 'Technology' + ',' + 'rating' + ', ' + 'Plays' + '\n')
    f.close()

    file = open('info.csv', 'a', encoding='utf-8')
    write_obj = csv.writer(file)



    for i in range(len(items_in_container)):

        gameName = items_in_container[i].find('div').img['alt']
        technology = items_in_container[i].find_all('a')[1].find('div', {'class': 'technology'}).text.strip().replace('\n', '')
        rating = items_in_container[i].find_all('a')[1].find('p', {'class': 'rating'}).text.strip().replace('\n', '')
        plays_count = items_in_container[i].find_all('a')[1].find('p', {'class': 'plays-count'}).text.strip().replace('\n', '')
        info_list = [gameName, technology, rating, plays_count]

        write_obj.writerow(info_list)





    p['page'] += 1
    time.sleep(random.randint(15, 20))