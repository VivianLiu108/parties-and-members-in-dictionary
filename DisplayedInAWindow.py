from urllib.request import urlopen
from bs4 import BeautifulSoup
from tkinter import *

window = Tk()
window.title("Legislative Yuan")

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

Label(window, text = "中國國民黨", bg = '#000095').grid(row = 0, column = 0)
Label(window, text = "民主進步黨", bg = '#1B9431').grid(row = 0, column = 1)
Label(window, text = "時代力量", bg = '#F9BE01').grid(row = 0, column = 2)
Label(window, text = "無黨籍", bg = '#999999').grid(row = 0, column = 3)
Label(window, text = "台灣民眾黨", bg = '#28C8C8').grid(row = 0, column = 4)
Label(window, text = "台灣基進", bg = '#A73f24').grid(row = 0, column = 5)

i = 0
for mem in parties:
    Label(window, text = parties[mem]).grid(row = 1, column = i, sticky = N)
    i+=1

window.mainloop()