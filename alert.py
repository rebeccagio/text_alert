import smtplib

import xlrd
import csv
import pandas as pd
from email.message import EmailMessage
# from email.MIMEText import MIMEText

def find_carrier(phone, carrier): 
    email = ''
    att = '@mms.att.net'
    boost = '@myboostmobile.com'
    cricket = '@mms.cricketwireless.net'
    google_fi = '@msg.fi.google.com'
    sprint = '@pm.sprint.com'
    straight_talk = '@mypixmessages.com'
    t_mobile = '@tmomail.net'
    tracfone = '@mmst5.tracfone.com'
    us_cellular = '@mms.uscc.net'
    verizon = '@vzwpix.com'
    virgin_mobile = '@vmpix.com'

    if carrier == "att": 
        email = phone + att
    elif carrier == 'boost':
        email = phone + boost
    elif carrier == 'cricket':
        email = phone + cricket
    elif carrier == 'google fi':
        email = phone + google_fi
    elif carrier == 'sprint':
        email = phone + sprint
    elif carrier == 'straight talk':
        email = phone + straight_talk
    elif carrier == 't-mobile':
        email = phone + t_mobile
    elif carrier == 'tracfone': 
        email = phone + tracfone
    elif carrier == 'us_cellular':
        email = phone + us_cellular
    elif carrier == 'verizon':
        email = phone + verizon
    elif carrier == 'virgin_mobile':
        email = phone + virgin_mobile

    return email

#################################################
def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    

    user = "rebeccagio085@gmail.com"
    msg['from'] = user
    password = "lenckjihhkgncgiy"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
    server.quit()

if __name__ == '__main__':

    # Create a dataframe from csv
    df = pd.read_csv('projects\\address_book.csv', delimiter=',')
    # User list comprehension to create a list of lists from Dataframe rows
    contact_list = [list(row) for row in df.values]
    # Print list of lists i.e. rows
    print(contact_list)

    # dict = [

    #     {'name': 'rebecca', 
    #     'phone': '6262656501', 
    #     'carrier': 'att'}, 

    #     {'name': 'robin', 
    #     'phone': '8184478352',
    #     'carrier': 'boost'}
    # ]

    # for contact in dict: 
    #     phone = contact['phone']
    #     carrier = contact['carrier']
    #     print(phone)
    #     print(carrier)

    # "Wellspring Generation:", "Test for Audio Bible Study Text Alerts"
    subject = "Wellspring Generation:"
    body = 'Click to start or join a scheduled Zoom meeting: ' + 'https://zoom.us/j/8383264131?pwd=eUJJMkpkdGIzRTNPcyt2aXNGcXJFQT09'

    for contact in contact_list: 
        phone = str(contact[1])
        carrier = str(contact[2])
        email = find_carrier(phone, carrier)
        print(email)
        email_alert(subject, body, email)


# upload csv file 
# enter "Subject", "Body", 
# send email alert -> click button 



