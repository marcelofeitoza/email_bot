import smtplib

sender = input("Who is sending this email?\n")
sender_password = input("OK. Now tell me this email password?\n")
recipient = input("Who is going to receive this email?\n")
message = input("What do you want this person to read?\n")

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(f'{sender}', f'{sender_password}')
server.sendmail(f'{sender}', f'{recipient}', f'{message}')

print('Email sent. Wait for the answer!!')