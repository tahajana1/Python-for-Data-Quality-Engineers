from datetime import date, datetime
import random

options = ["News", "Private ad", "Joke of the Day"]

user_input = input("Choose one of the three options (News, Private ad, Joke of the Day): ")

while user_input not in options:
    print("invalid option. Please try again")
    user_input = input("Choose one of the three options: (News, Private ad, Joke of the Day) ")

print("You selected: ", user_input)

if user_input == "News":
    txt = input("Please provide text: ")
    cty = input("please provide city: ")
    print("News..............")
    print(txt)
    today = date.today()
    print(cty, today.strftime("%B %d, %Y") )


if user_input == "Private ad":
    txt = input("Please provide your ad: ")
    while True:
        exp= input("please provide ad expiry date in format YYYYMMDD: ")
        try:
            date = datetime.strptime(exp, "%Y%m%d")
            break
        except ValueError:
            print("invalid date format. Please try again")
    print("Valid date: ",date)
    today = date.today()
    diff = (date - today).days
    print("Private ads..............")
    print(txt)
    print("Ad expiry date: ", date, ", ", diff, " days left")

if user_input == "Joke of the Day":
    txt = input("Please provide a funny joke: ")
    print("Joke of the Day................")
    print(txt)
    print("Funny meter: ", random.randint(1,10),"/10"  )
