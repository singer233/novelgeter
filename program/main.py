import requests
from bs4 import BeautifulSoup
from rzlib import rzlib

#for rizhao web
def main():

    try:
            fl = open('novel.txt',mode='w',encoding='utf-8')
    except:
            print('Can not creat the file')
    fl = open('novel.txt',mode='w',encoding='utf-8')
    try:
            url = open('website.txt', mode='r',encoding='utf-8')
            temptext = url.readline()
    except FileNotFoundError:
            temptext = input('please enter the website\n')
    rzlib(temptext.rstrip(),fl)
    fl.close()
main()