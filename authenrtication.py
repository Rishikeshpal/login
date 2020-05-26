import requests

url = 'https://mail.google.com/'
values = {'username': 'uremail',
          'password': 'password'}
r = requests.post(url, data=values)
#print (r.content)
status = str(r.content)
if "FailedLoginException" in status:
    print("Login failed! password might be wrong!")
elif "Super User" in status:
    print("200" + " login success")
else:
    print("Login failed! password might be wrong!")
