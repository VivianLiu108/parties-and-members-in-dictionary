#!/usr/bin/env python
# coding: utf-8

# In[11]:


from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://lilina.csie.ncnu.edu.tw/~solomon/NCNU/ly.html"
html = urlopen(url).read().decode('UTF-8')
bsObj = BeautifulSoup(html,"html.parser")
nameList = bsObj.findAll("div",{"class":"legislatorname"},{"style":"text-align: center;"})

for name in nameList:
    print(name.get_text())


# In[ ]:





# In[ ]:




