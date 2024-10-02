import datetime as dt
import random
import smtplib

day_of_week = dt.datetime.now().weekday()
print(day_of_week)
my_email = "bhumitexr@gmail.com"
my_password = "eomznfzhqgolwmrv"

if day_of_week == 6:
    with open("quotes.txt", mode="r") as quotes:
        lines = quotes.readlines()
        final_quote = random.choice(lines)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="bhumitr6333@gmail.com", msg="Subject: Mondays Motivation\n\n"
                                                                                      f"{final_quote}")


