'''
#auto mail function for training state report
# Subject: Auto_report_Success/Error_time
# Account: Auto_reporter@gmail.com Key: Auto_reporter
#
#2020/08/26
#Mingzhen Shao
'''


'''
Content:
    SUCCESS!/ERROR!
    Success: The training has been finished successfully, the result...
        the result includes loss, loss img, 
    Error: The training has been stoped. Error info: 
'''

import os, time

import smtplib

smtp = smtplib.SMTP()       #smtplib.SMTP('smtp.163.com', 25)   #also works
smtp.connect('smtp.163.com', 25) 

username = "s13@163.com"
password = ""

sender = "s13@163.com"
receiver = ["m14@gmail.com"]

message = '''From: SMZ <s13@163.com>
To: Mingzhen <m14@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
'''

smtp.login(username, password) 
smtp.sendmail(sender, receiver, message) 
smtp.quit()

def auto_mail_reporter(state, info):
    pass
    

