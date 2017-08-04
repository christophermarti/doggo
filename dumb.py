import requests
import json
import webbrowser

request = requests.get('https://dog.ceo/dog-api/')
response = requests.post('https://dog.ceo/api/breeds/list')

doggo = input("Doggo: ")
requested_doggo = json.loads(requests.post('https://dog.ceo/api/breeds/list').text)

if doggo in requested_doggo['message']:
    requested_images = requests.post('https://dog.ceo/api/breed/{0}/images'.format(doggo))
    image_results = json.loads(requested_images.text)
    print(request.url)
    print(response)
    print (image_results)
    print ("incoming ", doggo, " pics!\ngood boy! bork!")
    from time import sleep
    sleep(5)
    for doge in image_results['message']:
        webbrowser.open(doge)
else:
    print("ruh roh! we didn't find any ", doggo, "pics!")
