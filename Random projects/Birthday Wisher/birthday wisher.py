import datetime as dt
import random
import smtplib
import pandas

today = (dt.datetime.now().month, dt.datetime.now().day)
print(today)
my_email = "bhumitexr@gmail.com"
my_password = "eomznfzhqgolwmrv"

data = pandas.read_csv("../birthday-wisher-extrahard-start/birthdays.csv")

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today in birthday_dict:
    read = data.values.tolist()
    birthday_person = birthday_dict[today]
    with open(f"../birthday-wisher-extrahard-start/letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
        lines = letter.read()

        x = lines.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"],
                            msg="Subject: Happy Birthday\n\n"
                            f"{x}")
