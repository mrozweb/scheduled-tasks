import os
import random
import smtplib
import datetime as dt

MY_EMAIL = "deboerbeata@gmail.com"
PASSWORD = "ibfdodlwkwqhoyrx"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 6:
    with open("quotes.txt") as file:
        quotes = [quote.strip() for quote in file.readlines()]
        random_quote = random.choice(quotes)

    with smtplib.SMTP('smtp.gmail.com') as connection:
        # This code makes connection secure
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL ,
            to_addrs="doradada84@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{random_quote}"
        )
