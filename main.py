import requests
from bs4 import BeautifulSoup

target_url = "https://atilsamancioglu.com/"
response = requests.get(target_url)
data = response.text 

#html parsing
soup = BeautifulSoup(data, "html.parser")     #BeautifulSoup parses the HTML
all_a = soup.find_all('a') #search the HTML
for link in all_a:
    print(link.get("href"))