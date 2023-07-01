import requests
import bs4
import random as ran
import keyboard
user_input = True
while True :
    print("Press 1 for science , 2 for love  and 3 for life quotes")
    print("press esc to exit")
    if keyboard.is_pressed('escape'):
        print("Good bye ")
        user_input = 0
        break
    user=int(input("What kind of quote you want to read ??\t"))

    if 0<user<4 :

        break
    else :
         print("Please enter a vaild value")
         continue

if user == 1:
        user=str(user)
        user="science"
if user== 2 :
        user=str(user)
        user="love"
if user == 3 :
        user = str(user)
        user = "life"

def print_quotes () :
    randomPage=ran.randint(0,100)
    print("Selected Page :" + str(randomPage))
    web_site = requests.get("https://www.goodreads.com/quotes/tag/"+user+"?page="+str(randomPage))
    html = web_site.text
    htmlBl = bs4.BeautifulSoup(html, "lxml")
    quoates = htmlBl.findAll("div", attrs={"class": "quoteText"})
    randomN = ran.randint(0,30)
    print("Selected Quote : " + str(randomN))
    quoteSelected=quoates[randomN].text
    print(quoteSelected)
    return quoates
if user_input == True :
 print_quotes ()



