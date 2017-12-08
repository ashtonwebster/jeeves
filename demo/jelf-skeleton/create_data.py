import requests

SESSION_ID = "vrxoa0l5xmonxewzijktcnww03oftt1t"

for i in range(900):
    cookie = dict(sessionid = SESSION_ID)

    r = requests.get('http://localhost:8000/password', cookies=cookie);

    print(r.text)
    print(r.cookies)
    cookie['csrftoken'] = r.cookies['csrftoken']

    r = requests.post('http://localhost:8000/password', 
            data = {'csrfmiddlewaretoken' : r.cookies['csrftoken'],
                    'url' : 'someurl.com',
                    'username' : 'myusername.com',
                    'password' : 'supersecret' },
            cookies=cookie)

    print("\n\nRESPONSE:");
    print(r.text[:1000]);
