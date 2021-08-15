import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('alobiddut1234@gmail.com','ilovealoab')
server.sendmail('alobiddut1234@gmail.com','sarkerbiddut14@gmail.com','hii')