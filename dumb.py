import requests
import json
import webbrowser
import sys
from time import sleep

request = requests.get('https://dog.ceo/dog-api/')
print(request.url)
response = requests.post('https://dog.ceo/api/breeds/list')
print(response)

def greeting(): 
    print("Bork! Welcome to the Doggo Database!")
    print("What would you like to do?")
    print("*press [1] to see a list of doggos!")
    print("*press [2] to search for pics of a specific good boy!")
    print("*press [3] to quit! WOOF!")

def list():
    all_doggos = json.loads(requests.post('https://dog.ceo/api/breeds/list/all').text)
    for dog in all_doggos['message']:
        print(dog)
    print("\n" + "do you want to see pics of any doggos in the list?")
    choice = input("*press [1] to select a doggo! \n*press [2] to go back to the menu! \nChoice: ")
    if choice.isnumeric() == False:
        print("rruff! use numbers stoopid!")
        choice = input("try again: ")
    elif choice == "1":
        doggo = input(print("doggo: "))
        pics(doggo)
    else:
        print("\n")
        greeting()
        menu(choice = input("Choice: "))

def pics(doggo): 
    requested_doggo = json.loads(requests.post('https://dog.ceo/api/breeds/list').text)
    if doggo in requested_doggo['message']:
        requested_images = requests.post('https://dog.ceo/api/breed/{0}/images'.format(doggo))
        image_results = json.loads(requested_images.text)
        print (image_results)
        print (len(image_results['message']),"incoming ", doggo, " pics!\ngood boy! bork!")
        sleep(3)
        for doge in image_results['message']:
            webbrowser.open(doge)
    else:
        print("ruh roh! we didn't find any ", doggo, "pics!")

def menu(choice):
    if choice.isnumeric() == False:
        print("rruff! use numbers stoopid!")
        menu(choice = input("Try again: "))
    elif choice == "1":
        list()
    elif choice == "2": 
        pics(doggo = input("Doggo: "))
    elif choice == "3":
        print("GOODBYE!")
        sad_doge="""\
                                      ,.  , 
                          .-. \ \| \ 
             ,---._    _,-.> `.\ \ ( 
            (__,'  `   `>-         -\ 
                     ,-'             `-. 
         ,-'       ,  ,    .       .    `. 
       ,'\       ,' ,-'    `-.      ;    :`. 
      (__;     ,',,'      ,   `     : `. :  \ 
             ,' |  _,'   /_    `    :  ; :   \ 
            /  ,',' |   /  \        '     ;   \ 
           /   | |(o|  /  (o)          |  |    ; 
          /     ___-^-^-----.          |  |    | 
         (   ,---. `-.           :.    |       : 
          ;,'      )  `          :..   |        | 
          :\      /              :.    |        ; 
          :.`-.__,              ,:`    |        | 
          ;`.    .             ':'      \      , 
         /   `-.__\           '      ,   \     \. 
        (   ,'    \`--,-----.       /     \     \`. 
         `-'       \,' ,'   /    / |       \     | `. 
      -hrr-        /  '   ,'    /-.|        `.   ;   `. 
                  (      /`----'   |          `--'     ` 
                   `.__,' 
                          
        """
        print(sad_doge)
        sleep(0.75)
        sys.exit
    else:
        print("rrruf! try again!")

greeting()
menu(choice = input("Choice: "))
