import os
import random
import smtplib
import datetime as dt

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open("quotes.txt") as file:
        quotes = [quote.strip() for quote in file.readlines()]
        random_quote = random.choice(quotes)

    with smtplib.SMTP('smtp.gmail.com') as connection:
        # This code makes connection secure
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL ,
            to_addrs="deboerbeata3@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{random_quote}"
        )
