import bs4
import requests

url = 'http://jadwalsholat.pkpu.or.id/monthly.php?id=233'
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}
contents = requests.get(url, headers= headers)

response = bs4.BeautifulSoup(contents.text, 'html.parser')

data = response.find_all('tr', 'table_highlight')
data = data[0]

sholat = {}
i = 0
for d in data:
  if i == 1:
    sholat['shubuh'] = d.get_text()
  if i == 2:
    sholat['dzuhur'] = d.get_text()
  if i == 3:
    sholat['ashar'] = d.get_text()
  if i == 4:
    sholat['maghrib'] = d.get_text()
  if i == 5:
    sholat['isya'] = d.get_text()
  i +=1

print(sholat['ashar'])