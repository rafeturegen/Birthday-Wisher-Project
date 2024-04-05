##################### Hard Starting Project ######################
import smtplib

# 1. Update the birthdays.csv with your friends & family's details. 


# 2. Check if today matches a birthday in the birthdays.csv


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas
import datetime as dt
import random
my_email = "rafetcode@gmail.com"
password = "uqaogqvgbgvwrlln"
PLACEHOLDER = "[NAME]"
now = dt.datetime.now()
month = now.month
day = now.day

data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")
if data_dict[0]["month"] == month and data_dict[0]["day"] == day:
    random_number = random.randint(1, 3)
    with open(f"letter_{random_number}.txt") as letter:
        letter_content = letter.read()
        completed_letter = letter_content.replace(PLACEHOLDER, data_dict[0]["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="rafetcode@yahoo.com", msg=f"Subject:Happy Birthday\n\n{completed_letter}")

