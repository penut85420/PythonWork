import requests

url = "https://lol.garena.tw/game/champion"
soup = BeautifulSoup(requests.get(url, cookies=COOKIES).text, "html5lib")
