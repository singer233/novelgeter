from tool import *
import requests
from bs4 import BeautifulSoup

def rzlib(url,fl) :
    url_base = 'https://www.rzlib.net'
    html = gethtml(url)
    chapter_pages = []
    chapter_title = []
    soup = BeautifulSoup(html,"lxml")
    page_1 = soup.find_all('div',{'class':"ListChapter"})[1] #find the chapter pages for the novel in the div
    page_2 = page_1.find_all('li') #break the div
    for a in page_2: #break the li
        for href in a.find_all('a'): 
            chapter_pages.append(url_base+href['href']) #get href in the a to get the chapter pages
            chapter_title.append(href.string)
    pagenumber = len(chapter_title)
    currentpage = int(0)
    if len(chapter_pages)!=len(chapter_title):
            print('what')
    for x,y in zip(chapter_title,chapter_pages):
        filewrite('\n'+x,fl)
        rzlib_onepage(y,fl)
        currentpage=currentpage+1
        print('percent: {:.2f}%'.format((currentpage/pagenumber)*100))

def rzlib_onepage(url,fl):
    html = gethtml(url)
    soup = BeautifulSoup(html,"html5lib")
    text_1 = soup.find_all('div',{'id':"chapter_content"})[0]
    text = text_1.contents
    line = False
    for a in text:
        if a.string!=None:
               filewrite(a.string,fl)
               line=False
        elif line==False:
               filewrite('\n',fl)
               line=True  
