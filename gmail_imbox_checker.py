from imbox import Imbox
import html2text

class gmail_checker:
    
    def get_emails(self, email_user, password_user, mark_seen=False):
        self.email_user = email_user
        self.password = password_user
        
        with Imbox('imap.gmail.com',
                   username=self.email_user,
                   password=self.password,
                   ssl=True,
                   ssl_context=None,
                   starttls=False) as imbox:
            
            h = html2text.HTML2Text()
            h.ignore_links = True
            h.ignore_images = True
            
            self.all_inbox_messages = imbox.messages(unread=True)
            print(self.all_inbox_messages)
            
            self.emails = list()
            for uid, message in self.all_inbox_messages:
                if message.sent_from[0]['email'] == 'notificacion@notificacionesbaccr.com':            
                    self.output = (h.handle(f'''{message.body}''').replace("\\r\\n", ""))
                    self.output = self.output.replace("\n", "")
                    self.mail_body = self.output[2:-2]
                    
                    self.email = {
                        'id': uid,
						'sent_from': message.sent_from[0]['email'],
						'subject': message.subject,
						'Message': self.mail_body
					}
                    
                    self.emails.append(self.email)
                    
                    if mark_seen == True:
                        imbox.mark_seen(uid)
                        print('All reviewed emails were put on seen')
            
        return self.emails