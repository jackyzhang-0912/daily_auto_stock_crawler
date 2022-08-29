#!/usr/bin/env python3.9
import smtplib
import time
from email.mime.text import MIMEText
from email.utils import formataddr
from datetime import date
from urllib import response
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# sender's email address
sender='992530621@qq.com'  
# sender's email smtp cpde
smtp_code = ''   
# receiver's email address
receiver='jackyzhang0912@gmail.com'


def sendMail(stockDict):
  ret=True
  try:
    emailBody = ''
    for key in stockDict:
      emailBody += (getStockData(key, stockDict[key], True))  # currency needs work!!! Hard-coded for now
    # content of the email
    msg=MIMEText(emailBody,'plain','utf-8') 
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
  except Exception as e: 
    print(e)
    ret=False

  return ret

def getStockData(stockName, stockUrl, isForeignCurrency):
  browser.get(stockUrl)
  # time.sleep(17)
  stock_price = browser.find_element("xpath", '//div[@class="zxj"]').text
  stock_change_amount = browser.find_element("xpath", '//div[@class="zd"]/span[1]').text
  stock_change_percent = browser.find_element("xpath", '//div[@class="zd"]/span[2]').text
  if isForeignCurrency:
    stock_currency = browser.find_element("xpath", '//span[@class="quote_title_money"]').text[5:]
    return ('The stock price of ' + stockName + ' is ' + stock_price + '; ' + 'change percent is ' 
    + stock_change_percent + ' with an amount change of ' + stock_change_amount + '; ' 'The currency used is ' + stock_currency + '\n')
  return ('The stock price of ' + stockName + ' is ' + stock_price + '; ' + 'change percent is ' 
    + stock_change_percent + ' with an amount change of ' + stock_change_amount + '\n')

  

# dictionary contains stocks' names and corresponding urls
stockDict = {"Tencent" : "https://quote.eastmoney.com/hk/00700.html"}
service = Service('/Users/skywalker/Downloads/chromedriver')
browser = webdriver.Chrome(service=service)


ret=sendMail(stockDict)
if ret:
  print("Send successfully")
else:
  print("Send failed")

browser.close()