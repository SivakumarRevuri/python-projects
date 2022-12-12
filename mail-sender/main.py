import smtplib

email_id = 'sivakumarr96@gmail.com'
email_pass = 'Lakshmi@123'

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:  # 587 is port number
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    # ehlo is an alternative to helo for services that support the smtp service extensions
    # in any case helo or ehlo is must command for the smtp client to commence  a mail transfer

    smtp.login(email_id, email_pass)

    subject = 'mail test'
    body = 'body goes here ....'

    msg = f'Subject: {subject} \n\n\n {body}'
    smtp.sendmail(email_id, 'sreelakshmiveerapu80@gmail.com', msg)

    # format here is sender's mail id ==
    