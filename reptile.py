# -*- coding: utf-8 -*-
# https://list.jd.com/list.html?cat=670,671,672
# https://list.jd.com/list.html?cat=670,671,672&page=6
import re
import urllib.request

def craw(url, page):

    html1=urllib.request.urlopen(url).read()
    html1=str(html1)
    pat1='<div id="plist".+? <div class="page clearfix">'
    result1=re.compile(pat1).findall(html1)
    result1=result1[0]
    pat2='<img width="220" height="220" data-img="1" data-lazy-img="//(.+?\.jpg)">'
    imagelist=re.compile(pat2).findall(result1)
    x=1
    for imageUrl in imagelist:
        imagename="D:/work/learnPython/image/"+str(page)+str(x)+".jpg"
        imageUrl="http://"+imageUrl
        print("imagename = %s,imageurl=%s\n" % (imagename,imageUrl))
        try:
            urllib.request.urlretrieve(imageUrl, filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print("e.code=",e.code)
                x+=1
            if hasattr(e, "reson"):
                print("e.reson=", e.reson)
                x+=1
        x+=1


def main():
	#主函数
	for i in range(1,5):
		url = "https://list.jd.com/list.html?cat=670,671,672&page="+str(i)
		craw(url, i)

if __name__ == '__main__':
	main()		