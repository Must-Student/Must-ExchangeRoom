#!/usr/bin/env python3
# coding:utf-8
import pymysql
from SendMail import *
sqlservername='SQLSERVERHERE'
sqluser='USERNAMEHERE'
sqlpasswd='PASSWORDHERE'
sqldatabase='DATABASENAMEHERE'

def GetDataBaseData():
    db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)
    check = db.cursor()
    sql = "select EmailAddress,BackupEmailAddress from ExchangeRoom.AccountInfo"
    check.execute(sql)
    db.commit()
    RawData=check.fetchall()
    db.close()
    return RawData


Content='''
<p>您好，为了方便您快速找到适配的房源，也为了系统能快速通知您已匹配成功，请加群1029840528。<br>
<p>也可直接<a target="_blank" href="https://qm.qq.com/cgi-bin/qm/qr?k=wCGSrEHBbTI9XytfwRw-4bUilAp4xLwJ&jump_from=webapi">点此加群</a>。
'''

if __name__ == '__main__':
    UerEmailInfos=GetDataBaseData()
    for UserInfos in UerEmailInfos:
        for EmailAddress in UserInfos:
            if EmailAddress!=None:
                send_mail_html(EmailAddress,'MUST-换寝系统：请加群以便快速匹配',Content)
    print('广播完毕')
