from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://lilina.csie.ncnu.edu.tw/~solomon/NCNU/ly.html"
html = urlopen(url).read().decode('UTF-8')
bsObj = BeautifulSoup(html,"html.parser")
nameList = bsObj.findAll("div",{"class":"legislatorname"},{"style":"text-align:center;"})
party = bsObj.findAll("img",{"class":"six-party-icon"})

parties = {}

for i in range(len(nameList)):
    parties[party[i].get("alt").strip("徽章")] = 0

for i in range(len(nameList)):
    if parties[party[i].get("alt").strip("徽章")] == 0:
        parties[party[i].get("alt").strip("徽章")] = ' '*4+nameList[i].get_text()
    else:
        parties[party[i].get("alt").strip("徽章")] += '\n'+' '*4+nameList[i].get_text()

for mem in parties:
    print(mem)
    print(parties[mem])