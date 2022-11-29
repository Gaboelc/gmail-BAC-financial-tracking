from credentials import email as email_user, password as password_user
from gmail_imbox_checker import gmail_checker

import csv
import os

email_user = email_user
password = password_user

gmail = gmail_checker()

field_names = ['ID','Reference','Date','Commerce','Transaction_type','Transaction_ammount']
email_data = gmail.get_emails(email_user, password, mark_seen=True)

if os.path.isfile('./data.csv') == False:
    with open('data.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        csv_file.close()

for email in email_data:
    data = gmail.get_data(email)
    
    with open('./data.csv', 'a', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        
        writer.writerow(data)
        csv_file.close()