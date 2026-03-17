from datetime import date, datetime
import random
import os



def usr_input():
    text = ""
    options = ["News", "Private ad", "Joke of the Day"]

    user_input = input("Choose one of the three options (News, Private ad, Joke of the Day): ")

    while user_input not in options:
        print("invalid option. Please try again")
        user_input = input("Choose one of the three options: (News, Private ad, Joke of the Day) ")

    print("You selected: ", user_input)
    if user_input == "News":
        txt = input("Please provide text: ")
        cty = input("please provide city: ")
        text += "News..............\n"
        text +=txt
        text += "\n"
        today = date.today()
        text = text +  cty + ", "
        text += today.strftime("%B %d, %Y")
        text += "\n\n\n\n"


    if user_input == "Private ad":
        txt = input("Please provide your ad: ")
        while True:
            exp= input("please provide ad expiry date in format YYYYMMDD: ")
            try:
                date1 = datetime.strptime(exp, "%Y%m%d").date()
                break
            except ValueError:
                print("invalid date format. Please try again")
        print("Valid date: ",date1)
        today = date.today()
        diff = (date1 - today).days
        text += "Private ads..............\n"
        text += txt
        text += "\n"
        text = text + "Ad expiry date: " + str(date1) + ", " + str(diff) + " days left\n\n\n\n"

    if user_input == "Joke of the Day":
        txt = input("Please provide a funny joke: ")
        text += "Joke of the Day................\n"
        text += txt
        text += "\n"
        text = text + "Funny meter: " +  str(random.randint(1,10)),"/10\n\n\n\n"
    return text
def file_ext():
    i = "yes"
    text = ""


    while i == "yes":
        print(usr_input())
        text = text + usr_input()
        inpt = input("Please provide if you want to add more: (yes/no): ")
        while inpt not in ("yes", "no"):
            print("invalid option. Please try again")
            inpt = input("Please provide if you want to add more: (yes/no): ")
        if inpt == "no":
            i = "no"
            with open("example.txt", "w") as f:
                f.write(text)

    print("done")

file_ext()
