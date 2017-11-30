# -*- coding: utf-8 -*-
# https://list.jd.com/list.html?cat=670,671,672
# https://list.jd.com/list.html?cat=670,671,672&page=6
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36
import re
import urllib.request

def craw(url, page):
    try:
        html1 = urllib.request.urlopen(url).read()
        html1 = str(html1)
    except urllib.error.URLError as e:
        return

    pat1='<div class="main-content--specify">.+? alt="qrcode">'
    # <div class="detail-qrcode">
    # <div class="app-detail-conts-inner-header">
    result1=re.compile(pat1).findall(html1)
    result1=result1[0]
    print('result =',result1)
    pat2='<img src="(.+?\.jpg)" alt="qrcode">'
    imagelist=re.compile(pat2).findall(result1)
    print('imagelist = ',imagelist)
    x=1
    for imageUrl in imagelist:
        imagename="D:/work/learnPython/image/"+str(page)+str(x)+".jpg"
        # print("imagename = %s,imageurl=%s\n" % (imagename,imageUrl))
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
    # 经我测验，知晓程序最多就3525个小程序。2017年11月30日
	for i in range(1,50000):
		url = "https://minapp.com/miniapp/"+str(i)
		craw(url, i)

if __name__ == '__main__':
	main()		