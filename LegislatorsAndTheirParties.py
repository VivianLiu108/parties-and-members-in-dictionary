from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://lilina.csie.ncnu.edu.tw/~solomon/NCNU/ly.html"
html = urlopen(url).read().decode('UTF-8')
bsObj = BeautifulSoup(html,"html.parser")
nameList = bsObj.findAll("div",{"class":"legislatorname"},{"style":"text-align: center;"})
party = bsObj.findAll("img",{"class":"six-party-icon"})

for i in range(113):
    print(party[i].get("alt").strip("徽章"),end="")
    print(" "+nameList[i].get_text())

