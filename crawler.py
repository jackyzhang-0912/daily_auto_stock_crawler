#!/usr/bin/env python3.9
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
# sender's email address
sender=''  
# sender's email smtp cpde
smtp_code = ''   
# receiver's email address
receiver=''   
def mail():
  ret=True
  try:
    # content of the email
    msg=MIMEText('Testing!','plain','utf-8') 
    # sender's nickname and email address
    msg['From']=formataddr(["jackyQQ",sender]) 
    # receiver's nickname and email address
    msg['To']=formataddr(["jackyGmail",receiver])       
    # subject of the email
    msg['Subject']="super crawler"        
    server=smtplib.SMTP_SSL("smtp.qq.com", 465) 
    # using smtp code to login
    server.login(sender, smtp_code) 
    server.sendmail(sender,[receiver,],msg.as_string())
    # close connection
    server.quit() 
    # if codes in try didn't run, ret will be set to false 
  except Exception: 
    ret=False

  return ret

ret=mail()
if ret:
  print("Send successfully")
else:
  print("Send failed")