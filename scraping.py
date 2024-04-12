import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.amazon.in/s?k=i+phone&rh=n%3A1389401031&ref=nb_sb_noss"
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",'Accept-Language': 'en-US, en;q=0.5'}


data = {'title':[],'Price':[]}
r = requests.get(url,headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
#print(soup.prettify())
spans=soup.select("span.a-size-medium.a-color-base.a-text-normal")
prices = soup.select("span.a-price")
for span in spans:
    print(span.string)
    data["title"].append(span.string)

for price in prices:
    if not("a-text-price" in price.get("class")):
        if len(data["Price"]) != len(data["title"]):
            print(price.find("span").get_text())
            data["Price"].append(price.find("span").get_text())
        else:
            break

df = pd.DataFrame.from_dict(data)
df.to_excel("data.xlsx", index=False)