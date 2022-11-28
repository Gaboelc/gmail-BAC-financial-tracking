from imbox import Imbox
import html2text
from getpass import getpass

from credentials import email as email_user, password as password_user

email_user = email_user
password = password_user

with Imbox('imap.gmail.com',
        username=email_user,
        password=password,
        ssl=True,
        ssl_context=None,
        starttls=False) as imbox:
    
    h = html2text.HTML2Text()
    h.ignore_links = True
    h.ignore_images = True
    
    all_inbox_messages = imbox.messages()
    for uid, message in all_inbox_messages:
        
        if message.sent_from[0]['email'] == 'notificacion@notificacionesbaccr.com':
            
            output = (h.handle(f'''{message.body}''').replace("\\r\\n", ""))
            output = output.replace("\n", "")
            mail_body = output[2:-2]
            
            print(message.sent_from[0]['email'])
            #print(message.sent_to)
            print(message.subject)
            print(mail_body)
            print('--------------------------------')