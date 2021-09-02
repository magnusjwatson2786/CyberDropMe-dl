import requests, sys, concurrent.futures,time, os, re, platform
from bs4 import BeautifulSoup as bs

def extractlinks(self,url,skip):
    try:
        r=requests.get(url)
    except:
        print("Oops!", sys.exc_info()[0], f"Cant download from {url}")
        skip=True
    else:
        print(r.status_code)
        self.links=[]
        soup=bs(r.text, "html.parser")
        titlebar=soup.find("h1",{"id":"title"})
        title=titlebar.attrs["title"]
        # print(title)
        self.title=title
        imgdivs=soup.findAll("div",{"class":"image-container column"})
        for i in imgdivs:
            url=i.find("a",{"class":"image"}).attrs["href"]
            # print(url)
            size=int(i.find("p",{"class":"is-hidden file-size"}).text.split(" ")[0])
            # print(size)  
            self.links.append([url,size])
        self.total=len(self.links)

