import requests

url = 'https://httpbin.org/uuid'

def fetch(session,url):
    with sessiion.get(url) as response:
        print(response.json()['uuid'])
        with open('/tmp/tokencontent.txt','a') as tokenfile:
            tokenfile.write(response.json()['uuid']+'\n')

def main():
    with requests.Session() as session:
        fetch(session,url)

for n in range(10):
    main()
