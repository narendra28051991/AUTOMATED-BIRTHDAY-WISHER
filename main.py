from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "YOUR_EMAIL_ADDRESS"
PASSWORD = "YOUR_EMAIL_PASSWORD"
today_month = datetime.now().month
today_day = datetime.now().day
today = (today_month, today_day)

birthdays_file = pandas.read_csv("birthdays.csv")

birthdays_dict = {
    (data_row["month"], data_row["day"]): data_row for (index, data_row) in birthdays_file.iterrows()
}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"./letter_templates/letter_{random.randint(1, 3)}.txt"

    with open(file_path) as letter_file:
        contents = letter_file.read()
        new_content = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Birthday Card\n\n"
                f"{new_content}"
        )