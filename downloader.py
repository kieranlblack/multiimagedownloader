import random
import requests
import sys
import time

baseURL = 'xxxxx' # url to request
cookies = 'xxxxx' # cookie

# how ever many images there are + 1
for i in range(1, 791):
    currentURL = baseURL + 'page-image-' + str(i) + '.png'
    fileName = 'page' + str(i) + '.png'

    headers = { 'Connection': 'keep-alive', 'Referer': currentURL, 'Cookie': cookies, 'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br' }

    print('GETTING: ' + currentURL + ' --> ' + fileName)
    response = requests.get(currentURL, headers=headers, stream=True)

    if response.status_code == 200:
        with open(fileName, 'wb') as output:
            for chunk in response:
                output.write(chunk)
    else:
        print('ut oh code' + str(response.status_code))
        sys.exit()
    del response

    time.sleep(random.randint(5, 10))