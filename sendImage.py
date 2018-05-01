import requests,json
url = 'http://pi2tucultivo.dis.eafit.edu.co/'
files ={'file':open('1_1_1_2.jpg', 'rb')}
r=requests.post(url, files=files)