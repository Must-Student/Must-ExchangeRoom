#!/usr/bin/env python3
#coding:utf-8


import smtplib

from email.mime.text import MIMEText


mail_user = 'roomexchange@must-student.xyz'

mail_pass = 'passwordhere'


def send_mail(to_list, subject, content):
    me = "宿舍信息共享平台" + "<" + mail_user + ">"
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = me
    msg['to'] = to_list
    try:
        s = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
        #smtp地址以及端口号/SMTP address and port
        s.login(mail_user, mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        print(to_list,subject,content)
        return True
    except Exception as e:
        print (str(e))
        with open ('error.log','a') as f:
            f.write(str(e))
            f.write('\n')

        return False


def send_mail_html(to_list, subject, content):
    me = "宿舍信息共享平台" + "<" + mail_user + ">"
    msg = MIMEText(content, 'html', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = me
    msg['to'] = to_list
    try:
        s = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
        #smtp地址以及端口号/SMTP address and port
        s.login(mail_user, mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        print(to_list,subject,content)
        return True
    except Exception as e:
        print (str(e))
        with open ('error.log','a') as f:
            f.write(str(e))
            f.write('\n')

        return False
