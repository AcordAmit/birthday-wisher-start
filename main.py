##################### Extra Hard Starting Project ######################
import os
import smtplib
import datetime as dt
import random
import pandas

MY_EMAIL="testpython1966@gmail.com"
PASSWORD="uopffxjszehdifyg"

def wish_birthday(name, email):
    random_wish_file=random_file()
    with open(random_wish_file,'r') as f:
        content=f.read()
        content=content.replace('[NAME]',name)
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.starttls()
        smtp.login(MY_EMAIL,PASSWORD)
        smtp.sendmail(from_addr=MY_EMAIL,to_addrs=email,msg=f"Subject: Birthday Wish\n\n{content}")

def random_file():
    random_letter=random.randint(1,3)
    return f"letter_templates/letter_{random_letter}.txt"

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
data =pandas.read_csv("birthdays.csv")
for index, row in data.iterrows():
    if row["month"]==dt.datetime.today().month and row["day"]==dt.datetime.today().day:
        wish_birthday(row["name"], row["email"])

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv








