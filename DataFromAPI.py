#  import data from API To File
import requests

url = "https://covidtracking.com/api/v1/us/daily.json"
params = {
    "format": "csv"
}
Content = requests.get(url, params=params)
print(Content.text)

with open('data.csv', 'a+') as f:
    f.write(Content.text)
