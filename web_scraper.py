from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from csv import DictWriter
import csv

driver = webdriver.Chrome('C:/Users/Mobeen/Desktop/Programming Courses/Python-Courses/PythonBootcamp/chromedriver.exe')
driver.get("https://stats.nba.com/leaders/")
lis =[]

nba_players = {}

#response = requests.get().content
soup = BeautifulSoup(driver.page_source, "html.parser")
#soup = BeautifulSoup(response.text, "html.parser")
categories = soup.find(class_="player").find_next_siblings()
players = soup.find_all("td",{'class': 'player'})
### GET EACH CATEGORY ###
cater = {}
statistical = []
cat_list = []

for cat in categories:
    cat_list.append(cat.get_text())

mid = int(len(players)/2)
half_list = players[:mid]
### GET EACH STAT
for stat in half_list:
    for statistic in stat.find_next_siblings():
        statistical.append(statistic.get_text())
    mapped = zip(cat_list,statistical)
    mapped = tuple(mapped)
    cater = dict((x, y) for x, y in mapped)
    nba_players.update({stat.get_text(): cater})
    statistical.clear()

with open("nba_players.csv", "w") as file:
    headers = ['Player', 'Category', 'Stat']
    csv_writer = csv.writer(file)
    csv_writer.writerow(headers)
    for player in nba_players:
        for caters in nba_players[player]:
            csv_writer.writerow([player, caters, nba_players[player][caters]])

### GET EACH PLAYER ###


