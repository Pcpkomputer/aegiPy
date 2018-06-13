import re
import os
from io import BytesIO
import shutil
import requests


def reversed(array):
    ran=len(array)
    struct=[]
    for x in range(int(ran)-1,-1,-1):
        struct.append(array[x])
    return struct
    
if __name__=='__main__':
    __DIR='D:/manga/'
    req=requests.Session()
    link='https://www.mangahere.cc/manga/domestic_na_kanojo/'
    html=req.get(link, headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}).text
    content=re.findall(r"<span class=\"left\">\s+<a class=\"[^\"]+\"\s+href=\"([^\"]+)\">\s+([^<]+)</a>", str(html))
    content=reversed(content)
    for l,j in content:
        l=l.replace(r'//',r'http://')
        print('Downloading... '+l)
        filename=re.search(r"/([c\d\.]+)/$",str(l)).group(1)
        if not os.path.isdir(__DIR+filename):
            os.mkdir(__DIR+filename)
            htmls=req.get(l, headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}).text
            index=re.search(r'(\d+)</option>\s+<option\s+value=\"[^\"]+\">Featured</option>', str(htmls)).group(1)
            for x in range(1,int(index)+1):
                htmls=req.get(str(l)+str(x)+'.html',headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}).text
                imgfile=re.search(r"<img id=\"loading\"[^<]+<img\s+src=\"([^\"]+)\"\s+onload=\"loadImg",str(htmls)).group(1)
                imgfilename=re.search(r"([\d\w]+.jpg)",str(imgfile)).group(1)
                imgdata=req.get(imgfile,headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}).content
                with open(os.path.join(__DIR+filename+'/'+imgfilename), 'wb') as data:
                    data.write(imgdata)
                    print(imgfilename+' successfully downloaded')
        if os.path.isdir(__DIR+filename):
            ran=len(os.listdir(os.path.join(__DIR,filename)))
            if ran>0:
                print('Passing...')
                pass
            if ran==0:
                htmls=req.get(l, headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}).text
                index=re.search(r'(\d+)</option>\s+<option\s+value=\"[^\"]+\">Featured</option>', str(htmls)).group(1)
                for x in range(1,int(index)+1):
                    htmls=req.get(str(l)+str(x)+'.html',headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}).text
                    imgfile=re.search(r"<img id=\"loading\"[^<]+<img\s+src=\"([^\"]+)\"\s+onload=\"loadImg",str(htmls)).group(1)
                    imgfilename=re.search(r"([\d\w]+.jpg)",str(imgfile)).group(1)
                    imgdata=req.get(imgfile,headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}).content
                    with open(os.path.join(__DIR+filename+'/'+imgfilename), 'wb') as data:
                        data.write(imgdata)
                        print(imgfilename+' successfully downloaded')
              
