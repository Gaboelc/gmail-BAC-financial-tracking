from credentials import email as email_user, password as password_user
from gmail_imbox_checker import gmail_checker

email_user = email_user
password = password_user

gmail = gmail_checker()

print(gmail.get_emails(email_user, password))
print('------------------------------------------------------------------------------------------------')