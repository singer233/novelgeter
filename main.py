import requests
from bs4 import BeautifulSoup
#get html code from the weside
def gethtml(url):
    headers={'User-Agent':'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    webpage = requests.get(url,headers=headers)
    if webpage.status_code != 200 :
            exit(-1)
    return webpage.text
#for rizhao web
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
        print('percent: {:.2f}%'.format(currentpage/pagenumber))

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
def filewrite(string,fl):
    fl.write(string)

def main():
    fl = open('novel.txt',mode='w',encoding='utf-8')
    url = open('website.txt', mode='r',encoding='utf-8')
    temptext = url.read()
    rzlib(temptext.rstrip(),fl)
    fl.close()
main()