import requests
from bs4 import BeautifulSoup
#get html code from the weside
def gethtml(url):
    headers={'User-Agent':'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    return requests.get(url,headers=headers).text
#for rizhao web
def rzlib(url) :
    url_base = 'https://www.rzlib.net'
    html = gethtml(url)
    chapter_pages = []
    soup = BeautifulSoup(html,"lxml")
    page_1 = soup.find_all('div',{'class':"ListChapter"})[1] #find the chapter pages for the novel in the div
    page_2 = page_1.find_all('li') #break the div
    for a in page_2: #break the li
        for href in a.find_all('a'): 
            chapter_pages.append(url_base+href['href']) #get href in the a to get the chapter pages
    for x in chapter_pages:
        rzlib_onepage(x)
def rzlib_onepage(url):
    html = gethtml(url)
    soup = BeautifulSoup(html,"lxml")
    title_1 = soup.find_all('div',{'id':'chapter_title'})[0] #get the div for chapter title
    print(title_1)
    
rzlib_onepage('https://www.rzlib.net/b/62/62930/27471091.html')