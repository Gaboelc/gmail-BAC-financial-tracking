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
    
    def get_data(self, data):
        data_id = data['id']
        data = data['Message']
    
        self.commerce = data[data.find('Comercio:'):data.find('Comercio:')+30]
        self.date = data[data.find('Fecha:'):data.find('Fecha:')+30]
        self.card = data[data.find('VISA|'):data.find('VISA|')+24]
        self.reference = data[data.find('Referencia:|'):data.find('Referencia:|')+23]
        self.transaction_type = data[data.find('Tipo de Transacción:|'):data.find('Tipo de Transacción:|')+30]
        self.transaction_type = data[data.find('Tipo de Transacción:|'):data.find('Tipo de Transacción:|')+30]
        self.ammount = data[data.find('Monto:|'):data.find('Monto:|')+20]
    
        self.commerce_clean = self.commerce.split('|')
        self.commerce_clean = self.commerce_clean[1].split('-')
        self.commerce_clean = self.commerce_clean[0].replace(' ', '')
    
        self.date_clean = self.date.split('|')
        self.date_clean = self.date_clean[1].replace(' ', '')
    
        self.card_clean = self.card.split('|')
        self.card_clean = self.card_clean[1].replace(' ', '')
    
        self.reference_clean = self.reference.split('|')
        self.reference_clean = self.reference_clean[1].replace(' ', '')
    
        self.transaction_type_clean = self.transaction_type.split('|')
        self.transaction_type_clean = self.transaction_type_clean[1].replace(' ', '')
    
        self.ammount_clean = self.ammount.split('|')
        self.ammount_clean = self.ammount_clean[1].split(' ')
        self.ammount_clean = self.ammount_clean[2]
            
        self.data_clean = {
            'ID': data_id,
            'Reference': self.reference_clean,
            'Date': self.date_clean,
            'Commerce': self.commerce_clean,
            'Transaction_type': self.transaction_type_clean,
            'Transaction_ammount': self.ammount_clean
        }
            
        return self.data_clean
        
    