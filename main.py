# import smtplib
#
# my_email = "shadypython80@gmail.com"
# her_email = "shadypython80@yahoo.com"
# password = "tvmogelwldmubflz"
#
# with smtplib.SMTP("smtp.gmail.com") as connection: # connect to gmail server
#     connection.starttls()  # encrypts email during transport
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="shadypython80@yahoo.com",
#                         msg="Subject: test\n\nThis is a test for the body")

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# print(now)
# print(year)

import smtplib
import datetime as dt
import random

my_email = "shadypython80@gmail.com"
password = "tvmogelwldmubflz"
her_email = "shadypython80@yahoo.com"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("quotes.txt") as qoute_file:
        all_qoutes = qoute_file.readlines()
        qoute = random.choice(all_qoutes)
    print(qoute)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=her_email, msg=f"Subject: Monday Motivation\n\n"
                                                                        f"{qoute}")
