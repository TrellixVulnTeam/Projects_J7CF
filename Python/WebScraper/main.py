import requests
import pandas
from bs4 import BeautifulSoup

estate_list = []

for i in range(0, 30, 10):
    print(i)
    r = requests.get("http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s={}.html".format(i),
                     headers={
                         'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

    c = r.content
    soup = BeautifulSoup(c, "html.parser")

    all = soup.find_all("div", {"class": "propertyRow"})
    propertyRows = len(all)

    for i in range(propertyRows):
        d = {}
        d["Address"] = all[i].find_all("span", {"class": "propAddressCollapse"})[0].text
        d["Locality"] = all[i].find_all("span", {"class": "propAddressCollapse"})[1].text
        d["Price"] = all[i].find("h4", {"class": "propPrice"}).text.strip()

        try:
            area = all[i].find("span", {"class": "infoSqFt"}).text
            d["Area"] = area[:5]
        except AttributeError:
            d["Area"] = None

        try:
            fullBaths = all[i].find("span", {"class": "infoValueFullBath"}).text
            d["Full Baths"] = fullBaths
        except AttributeError:
            d["Full Baths"] = None

        try:
            halfBaths = all[i].find("span", {"class": "infoValueHalfBath"}).text
            d["Half Baths"] = halfBaths[0]
        except AttributeError:
            d["Half Baths"] = None

        estate_list.append(d)

df = pandas.DataFrame(estate_list)
df.to_csv("scrappedData.csv")
print(df)
