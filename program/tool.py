import requests
#get html code from the weside
def gethtml(url):
    headers={'User-Agent':'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    webpage = requests.get(url,headers=headers)
    if webpage.status_code != 200 :
            print('website error return code: '+ str(webpage.status_code))
            exit(-1)
    return webpage.text
def filewrite(string,fl):
    fl.write(string)