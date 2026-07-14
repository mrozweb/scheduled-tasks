# import smtplib
#
# my_email = "deboerbeata@gmail.com"
# password = "ibfdodlwkwqhoyrx"
#
# with smtplib.SMTP('smtp.gmail.com') as connection:
#     # This code make connection secure
#     connection.starttls()
#     connection.login(my_email, password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="deboerbeata3@gmail.com",
#         msg="Subject:Hello!\n\nThis is the body of my email."
#     )
# connection.quit()
# connection.close()
#****************************************************************************
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# day_of_birth = dt.datetime(year=1984, month=4, day=1, hour=6)
# print(day_of_birth)
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