#!/usr/bin/env python3
# coding:utf-8

import pymysql
import hashlib
def md5(password):
    password=password.encode(encoding='utf-8')
    hashedPassword=hashlib.md5()
    hashedPassword.update(password)
    return (hashedPassword.hexdigest())


sqlservername='servernamehere'
sqluser='usernamehere'
sqlpasswd='passwordhere'
sqldatabase='databasenamehere'

def CheckIfUserExist(emailaddress):
    db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)
    check = db.cursor()
    sql = 'select EmailAddress from ' + sqldatabase + '.AccountInfo where EmailAddress =' + "'" + emailaddress + "'"
    check.execute(sql)
    temp=check.fetchone()
    temp= list(str(temp).replace('(', '').replace(')', '').replace("'", "").split(','))
    if temp[0]==emailaddress:
        return 0
    else:
        return 1


def adduser(EmailAddress,UserName,ContactInfo,PassWord,IsVerified,Sex,Address,Model,IdealAddress,IdealModel,Note):
    db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)
    check = db.cursor()
    sql = "insert into ExchangeRoom.AccountInfo (EmailAddress,UserName,ContactInfo,PassWord,IsVerified,Md5,Sex,Address,Model,IdealAddress,IdealModel,Note,AssociateEmail,MyDeal) VALUES (" + "'" + EmailAddress + "'" + ","+"'" + UserName + "'" + ","+"'" + ContactInfo + "'" + ","+"'" + PassWord + "'" + ","+"'" + IsVerified + "'" + ","+"'" + str(md5(PassWord))+'2020' + "'" + ","+ "'" + Sex + "'"+ ","+"'" + Address + "'" + ","+"'" + Model + "'" + ","+"'" + IdealAddress + "'" + ","+"'" + IdealModel + "'" + ","+"'" + Note + "'"+ ","+"'" + EmailAddress + "'"+ ","+"'" + '0' + "'" + ")"
    check.execute(sql)
    db.commit()
    #SecSql="insert into ExchangeRoom.AccountInfo (Address,Model,IdealAddress,IdealModel,Note,AssociateEmail) VALUES ("+"'" + Address + "'" + ","+"'" + Model + "'" + ","+"'" + IdealAddress + "'" + ","+"'" + IdealModel + "'" + ","+"'" + Note + "'"+ ","+"'" + EmailAddress + "'"  + ")"
    #check.execute(SecSql)
    #db.commit()
    db.close()
    return 1

def CheckVerifyCode(VerifyCode,EmailAddress):
    db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)
    check = db.cursor()
    sql = 'select IsVerified from ' + sqldatabase + '.AccountInfo where EmailAddress =' + "'" + EmailAddress + "'"
    check.execute(sql)
    a = check.fetchone()
    a = list(str(a).replace('(', '').replace(')', '').replace("'", "").split(','))
    if a[0] == VerifyCode:
        return 1
    else:
        return 0

def UpdateIsVerified(EmailAddress,VerifyCode):
    db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)
    check = db.cursor()
    sql='update '+sqldatabase+'.AccountInfo set IsVerified='+VerifyCode+' where EmailAddress='+ "'" +EmailAddress+ "'"
    check.execute(sql)
    db.commit()
    db.close()
    return 1
def ReadMd5(EmailAddress):
    try:
        db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)
        check = db.cursor()
        sql = 'select Md5 from ' + sqldatabase + '.AccountInfo where EmailAddress =' + "'" + str(EmailAddress) + "'"
        # print(sql)
        check.execute(sql)
        a = check.fetchone()
        a = list(str(a).replace('(', '').replace(')', '').replace("'", "").split(','))
        # print(a)
        if a[0] is not None:
            return a[0]
        else:
            return 0
    except:
        return 0

def CheckEmailAddressPassWord(EmailAddress,PassWord):
    db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)
    check = db.cursor()
    sql = 'select PassWord from ' + sqldatabase + '.AccountInfo where EmailAddress =' + "'" + EmailAddress + "'"
    check.execute(sql)
    a = check.fetchone()
    a = list(str(a).replace('(', '').replace(')', '').replace("'", "").split(','))
    if a[0] == PassWord:
        return 1
    else:
        return 0

def ReturnAllData(Sex):
    db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)
    check = db.cursor()
    sql = "select UserName, Sex, Address, Model, ContactInfo, Note,IdealAddress, IdealModel, MyDeal from ExchangeRoom.AccountInfo where Sex="+"'"+Sex+"'"
    check.execute(sql)
    a = check.fetchall()
    #print(a)
    return a 

def ReturnSexFromEmail(EmailAddress):
    db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)
    check = db.cursor()
    sql = "select Sex from ExchangeRoom.AccountInfo where EmailAddress="+"'"+EmailAddress+"'"
    check.execute(sql)
    a = check.fetchone()
    return a[0]

def ReturnInfoFromSexAndModel(Sex,Model):
    db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)
    check = db.cursor()
    sql = "select UserName, Sex, Address, Model, ContactInfo, Note,IdealAddress, IdealModel, MyDeal from ExchangeRoom.AccountInfo where Sex="+"'"+Sex+"'"+" and Model="+"'"+Model+"'"
    check.execute(sql)
    a = check.fetchall()
    # print(a)
    return a

def ReturnInfoFromSexAndAddress(Sex,Address):
    db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)
    check = db.cursor()
    sql = "select UserName, Sex, Address, Model, ContactInfo, Note,IdealAddress, IdealModel, MyDeal from ExchangeRoom.AccountInfo where Sex=" + "'" + Sex + "'" + " and Address=" + "'" + Address + "'"
    check.execute(sql)
    a = check.fetchall()
    # print(a)
    return a

def ReturnInfoFromSexAndAddressAndModel(Sex,Address,Model):
    db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)
    check = db.cursor()
    sql = "select UserName, Sex, Address, Model, ContactInfo, Note,IdealAddress, IdealModel, MyDeal from ExchangeRoom.AccountInfo where Sex=" + "'" + Sex + "'" + " and Address=" + "'" + Address + "'"+ " and Model=" + "'" + Model + "'"
    check.execute(sql)
    a = check.fetchall()
    # print(a)
    return a

def ReturnInfoFromSexIdealAddressIdealModel(Sex,IdealAddress,IdealModel,Address,Model):
    db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)
    check = db.cursor()
    sql=''
    if IdealModel=='0':
        if IdealAddress=='0':
            sql="select EmailAddress, UserName, Sex, Address, Model, ContactInfo, Note,MyDeal from ExchangeRoom.AccountInfo where Sex=" + "'" + Sex + "'" + " and (IdealAddress='0' or IdealAddress=" + "'" + Address + "')"+ " and (IdealModel='0' or IdealModel=" + "'" + Model + "')"
        else:
            sql = "select EmailAddress, UserName, Sex, Address, Model, ContactInfo, Note,MyDeal from ExchangeRoom.AccountInfo where Sex=" + "'" + Sex + "'" + " and Address=" + "'" + IdealAddress + "'" + + " and (IdealAddress='0' or IdealAddress='" + "'" + Address + "')" + " and (IdealModel='0' or IdealModel=" + "'" + Model + "')"
    else:
        if IdealAddress=='0':
            sql = "select EmailAddress, UserName, Sex, Address, Model, ContactInfo, Note,MyDeal from ExchangeRoom.AccountInfo where Sex=" + "'" + Sex + "'" + " and Model=" + "'" + IdealModel + "'"  + " and (IdealAddress='0' or IdealAddress=" + "'" + Address + "')" + " and (IdealModel='0' or IdealModel=" + "'" + Model + "')"
        else:
            sql = "select EmailAddress, UserName, Sex, Address, Model, ContactInfo, Note,MyDeal from ExchangeRoom.AccountInfo where Sex=" + "'" + Sex + "'" + " and Address=" + "'" + IdealAddress + "'" + " and Model=" + "'" + IdealModel + "'" + " and (IdealAddress='0' or IdealAddress=" + "'" + Address + "')" + " and (IdealModel='0' or IdealModel=" + "'" + Model + "')"

    #print(sql)
    check.execute(sql)
    a = check.fetchall()
    # print(a)
    return a


def ReturnEmailAddressIsVerified(EmailAddress):
    db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)
    check = db.cursor()
    sql = "select IsVerified from ExchangeRoom.AccountInfo where EmailAddress=" + "'" + EmailAddress + "'"
    try :
        check.execute(sql)
        a=check.fetchone()
        if a[0]=='1':
            return 1
        else:
            return 0
    except:
        return 0


def ReturnInfoFromEmailAddress(EmailAddress):
    db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)
    check = db.cursor()
    sql = "select UserName, Sex, Address, Model, ContactInfo, Note,IdealAddress, IdealModel, MyDeal from ExchangeRoom.AccountInfo where EmailAddress=" + "'" + EmailAddress + "'"
    check.execute(sql)
    a = check.fetchone()
    # print(a)
    return a

def CheckEmailAddressAlreadyExist(EmailAddress):
    db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)
    check = db.cursor()
    sql = "select EmailAddress from ExchangeRoom.AccountInfo where EmailAddress=" + "'" + EmailAddress + "'"
    try:
        check.execute(sql)
        a = check.fetchone()
        print(a)
        if a[0]==EmailAddress:
            return 1
        if a[0]=='':
            return 0
    except:
        return 0

def UpdateUserInfo(UserName,ContactInfo,Address,Model,IdealAddress,IdealModel,Note,EmailAddress):
    db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)
    check = db.cursor()
    sql='update '+sqldatabase+'.AccountInfo set Username='+"'"+UserName+"',"+' ContactInfo='+"'"+ContactInfo+"',"+' Address='+"'"+Address+"',"+' Model='+"'"+Model+"',"+' IdealAddress='+"'"+IdealAddress+"',"+' IdealModel='+"'"+IdealModel+"',"+' Note='+"'"+Note+"'"+' where EmailAddress='+"'"+EmailAddress+"';"
    print(sql)
    check.execute(sql)
    db.commit()
    db.close()
    return 1

def UpdateBackupEmailAddressByEmailAddress(BackupEmailAddress,EmailAddress,IsVerified):
    db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)
    check = db.cursor()
    sql = 'update ' + sqldatabase + '.AccountInfo set BackupEmailAddress=' + "'" + BackupEmailAddress + "'," +' IsVerified='+ "'" + IsVerified + "'"+' where EmailAddress=' + "'" + EmailAddress + "'"
    print(sql)
    check.execute(sql)
    db.commit()
    db.close()
    return 1

def CheckBackupEmailAddressByEmailAddress(EmailAddress):
    db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)
    check = db.cursor()
    sql = 'select  BackupEmailAddress from ExchangeRoom.AccountInfo where EmailAddress=' + "'" + EmailAddress + "'"
    print(sql)
    check.execute(sql)
    a = check.fetchone()
    print(a)
    db.commit()
    db.close()
    if (a[0]=='') or (str(a[0])=='None'):
        return 0
    else:
        return 1
