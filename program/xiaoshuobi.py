from tool import *
import json
from bs4 import BeautifulSoup
base = 'https://www.xiaoshuobi.cc'
file_base = base+'/files/'
chapter_base = 'https://www.xiaoshuobi.cc/chapter.html?1#'
chapter_number = []
chapter_titles = []


def xiaoshuobi(html):
    get_chapter(html)
    for x in chapter_number:
        pass

def get_chapter(html):
    # get bookid
    bookid = html.replace(base+'/read/', "")
    # get chapters urls
    # get json for chapter id
    jsons = gethtml(file_base+bookid[0:5]+'/'+bookid+'/'+bookid+'.json')
    jsons = json.loads(jsons)
    for item in jsons['list']:  # jsons['list'] is a list
        # get chapter id to make chapter urls
        # item is a dictionary
        chapter_number.append(str(
            'https://www.xiaoshuobi.cc/chapter.html?1#bookid=%s&chapterid=%s' % (bookid, item['chapterid'])))
        chapter_titles.append(item['chaptername'])
def each_chapter(html):
    soup = BeautifulSoup(gethtml(html),'lxml')
    

if __name__ == "__main__":
    each_chapter('https://www.xiaoshuobi.cc/chapter.html?1#bookid=111979&chapterid=50698584')
