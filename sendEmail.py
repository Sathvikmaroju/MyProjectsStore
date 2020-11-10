import smtplib

s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("Sender_email_id",'Sender_email_id_password')
message = "message you want to send"
s.sendmail("Sender_email_id",'Receiver_email_id',message)
s.quit()