import requests,json
url = 'http://pi2tucultivo.dis.eafit.edu.co/'
files ={'file':open('1_1_1_2.jpg', 'rb')}
enviado=False
while enviado==False:
    r=requests.post(url, files=files)
    if r.status_code == 200:
        enviado=True
        print(r.status_code)