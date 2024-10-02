import smtplib

my_email = "bhumitexr@gmail.com"
my_password = "eomznfzhqgolwmrv"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs="bhumitr6333@gmail.com", msg="Subject: This is the subject\n\n"
                                                                                  "This is the body of my mail")


import datetime as dt

now = dt.datetime.now()
year = now.year
day_of_week = now.weekday()
print(day_of_week)

DOB = dt.datetime(year=2000, month=6, day=18)
print(DOB)