from credentials import email as email_user, password as password_user
from gmail_imbox_checker import gmail_checker

email_user = email_user
password = password_user

gmail = gmail_checker()

emails = gmail.get_emails(email_user, password, mark_seen=False)
for email in emails:
    email = email['Message']
    
    comerce = email[email.find('Comercio:'):email.find('Comercio:')+30]
    date = email[email.find('Fecha:'):email.find('Fecha:')+30]
    card = email[email.find('VISA|'):email.find('VISA|')+24]
    reference = email[email.find('Referencia:|'):email.find('Referencia:|')+23]
    transaction_type = email[email.find('Tipo de Transacción:|'):email.find('Tipo de Transacción:|')+30]
    transaction_type = email[email.find('Tipo de Transacción:|'):email.find('Tipo de Transacción:|')+30]
    ammount = email[email.find('Monto:|'):email.find('Monto:|')+17]
    
    comerce_clean = comerce.split('|')
    comerce_clean = comerce_clean[1].split('-')
    comerce_clean = comerce_clean[0].replace(' ', '')
    
    date_clean = date.split('|')
    date_clean = date_clean[1].replace(' ', '')
    
    card_clean = card.split('|')
    card_clean = card_clean[1].replace(' ', '')
    
    reference_clean = reference.split('|')
    reference_clean = reference_clean[1].replace(' ', '')
    
    transaction_type_clean = transaction_type.split('|')
    transaction_type_clean = transaction_type_clean[1].replace(' ', '')
    
    ammount_clean = ammount.split('|')
    ammount_clean = ammount_clean[1].split(' ')
    ammount_clean = ammount_clean[2]
    
    print(comerce_clean, date_clean, card_clean, reference_clean, transaction_type_clean, ammount_clean)