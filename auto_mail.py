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

smtp = smtplib.SMTP() 
smtp.connect('smtp.163.com,25') 

username = "smz13963229340@163.com"
password = "smz&&824"

sender = "smz13963229340@163.com"
receiver = ["mingzhen1993@gmail.com"]

message = '''\
Subject: Testing Mail

This is a testing message.
'''
smtp.login(username, password) 
smtp.sendmail(sender, receiver, message) 
smtp.quit()

def auto_mail_reporter(state, info):
    pass
    

