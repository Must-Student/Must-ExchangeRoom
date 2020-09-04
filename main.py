#!/usr/bin/env python3
# coding:utf-8
from flask import Flask, request, session, redirect, Response
import os
from HtmlSource import *
from DatabaseOperation import *
import random
from SendMail import *
from Functions import *
from MatchSystem import *

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
VerifyCode = '633305981'


def SendEmailToNotifyNewInfo(a, EmailAddress, UserName, Sex, Address, Model, ContactInfo, Note):
    for i in a:
        EmailAddress_NeedToSend = i[0]
        Subject = 'MUST-学生换租系统-您有新的可换租信息'
        Contenct = '以下是新增的符合您预留的换租信息，您也可以登录https://must-student.xyz 详细查询:\n邮箱地址 用户名 性别 房租地 房型 联系信息 备注 是否已交换成功(是则显示对方邮箱地址，否显示0)\n' + EmailAddress + ' ' + UserName + ' ' + Sex + ' ' + Address + ' ' + Model + ' ' + ContactInfo + ' ' + Note + ' ' + '0'
        send_mail(EmailAddress_NeedToSend, Subject, Contenct)

        print('收件人：', EmailAddress)
        print('正文：', Contenct)
    return 1


#@app.route('/verify', methods=['GET'])
#def verify_get():
    #    verify = request.cookies.get('verify')
    #   if verify == VerifyCode:
    #       return redirect('/signin')
    #   else:
#       return (VerifySourceCode)

@app.route('/verify', methods=['GET'])
def verify_get():
    return redirect('/signin')


#@app.route('/verify', methods=['post'])
#def verify_post():
    #    QQGroupID = str(request.form['QQGroupID'])
    #  if QQGroupID == VerifyCode:
    #      response = redirect('/signin')
    #      response.set_cookie('verify', QQGroupID, max_age=7 * 24 * 3600)
    #      return response
    # else:
#     return ('QQ群号不正确，认证失败<br>' + VerifySourceCode)


@app.route('/signin', methods=['GET'])
def signin_get():
    #verify = request.cookies.get('verify')
    EmailAddress = request.cookies.get('EmailAddress')
    Md5 = request.cookies.get('Md5')

    #if verify == VerifyCode:
    if str(ReadMd5(EmailAddress)) == Md5:
        return redirect('/mainpage')
    else:

        return (SigninSourceCode)
            #    else:
#        return redirect('/verify')


@app.route('/signin', methods=['post'])
def signin_post():
    verify = request.cookies.get('verify')
    #if verify == VerifyCode:
    EmailAddress = str(request.form['EmailAddress'])
    PassWord = str(request.form['PassWord'])
    try:
        if CheckEmailAddressPassWord(EmailAddress, PassWord):
            response = redirect('/mainpage')
            response.set_cookie('EmailAddress', EmailAddress, max_age=7 * 24 * 3600)
            response.set_cookie('Md5', ReadMd5(EmailAddress), max_age=7 * 24 * 3600)
            print('md5:', ReadMd5(EmailAddress))
            return response
        else:
            return ('邮件地址或者密码错误' + SigninSourceCode)
    except:
        return ('邮件地址或者密码错误' + SigninSourceCode)



#    else:
 #       return redirect('/verify')


@app.route('/signup', methods=['GET'])
def signup_get():
    #verify = request.cookies.get('verify')
    EmailAddress = request.cookies.get('EmailAddress')
    Md5 = request.cookies.get('Md5')
    #if verify == VerifyCode:
    if str(ReadMd5(EmailAddress)) == Md5:
        return redirect('/mainpage')
    else:
        return (SignupSourceCode)
    #else:
    #    return redirect('/verify')


@app.route('/signup', methods=['POST'])
def signup_post():
    #verify = request.cookies.get('verify')
    #if verify == VerifyCode:
    UserName = str(request.form['UserName'])
    EmailAddress = str(request.form['EmailAddress'])
    ContactInfo = str(request.form['ContactInfo'])
    Sex = str(request.form['Sex'])
    Address = str(request.form['Address'])
    Model = str(request.form['Model'])
    IdealAddress = str(request.form['IdealAddress'])
    IdealModel = str(request.form['IdealModel'])
    Note = str(request.form['Note'])
    PassWord = str(request.form['PassWord'])
    randomPort = str(random.randint(1000, 9999))
    IsVerified = str(randomPort)
    #print(UserName)
    #print(type(UserName))
    if (UserName =='') or (EmailAddress=='')or  (ContactInfo=='') or(Sex=='') or (Address=='') or ( Model=='') or (IdealAddress=='') or (IdealModel=='') or (PassWord==''):
        return ('姓名/邮箱地址/联系信息/性别/宿舍地址、类型/意向宿舍地址、类型/密码 都不能为空<br>'+SignupSourceCode)
    if EmailAddress.find('@') == -1:
        EmailAddress = EmailAddress + '@student.must.edu.mo'
    if CheckEmailAddressAlreadyExist(EmailAddress):
        return ('邮箱地址已注册过，请选择其他邮箱地址注册<br>'+SignupSourceCode)
    try:
        send_mail(EmailAddress, '请验证您的邮箱地址', '请将验证码填入网页以验证：' + randomPort)
    except:
        print(EmailAddress, '邮件发送失败')
    a = ReturnInfoFromSexIdealAddressIdealModel(Sex, IdealAddress, IdealModel, Address, Model)
    try:
        SendEmailToNotifyNewInfo(a, EmailAddress, UserName, Sex, Address, Model, ContactInfo, Note)

    except:
        print('提醒邮件邮件发送失败')
    adduser(EmailAddress, UserName, ContactInfo, PassWord, IsVerified, Sex, Address, Model, IdealAddress,
            IdealModel, Note)
    response = redirect('/VerifyEmail')
    response.set_cookie('EmailAddress', EmailAddress, max_age=7 * 24 * 3600)
    response.set_cookie('Md5', str(md5(PassWord)) + '2020', max_age=7 * 24 * 3600)
    return response

    #else:
    #    return redirect('/VerifyEmail')


@app.route('/VerifyEmail', methods=['GET'])
def VerifyEmail_get():
    #verify = request.cookies.get('verify')
    EmailAddress = request.cookies.get('EmailAddress')
    # UserName = request.cookies.get('UserName')
    PreInfo = '<p> 欢迎您 ' + EmailAddress + '<br>'
    #if verify == VerifyCode:
    return (PreInfo + VerifyEmailSourceCode)
    #else:
    #    return redirect('/verify')


@app.route('/VerifyEmail', methods=['POST'])
def VerifyEmail_post():
    #verify = request.cookies.get('verify')
    EmailAddress = request.cookies.get('EmailAddress')
    VerifyCode_YanZhengMa = str(request.form['VerifyCode'])
    # print(verify,EmailAddress,VerifyCode)
    #if str(verify) == str(VerifyCode) and EmailAddress is not None and VerifyCode_YanZhengMa is not None:
    if  EmailAddress is not None and VerifyCode_YanZhengMa is not None:
        if CheckVerifyCode(VerifyCode_YanZhengMa, EmailAddress):
            UpdateIsVerified(EmailAddress, '1')
            response = redirect('/mainpage')
            response.set_cookie('EmailAddress', EmailAddress, max_age=7 * 24 * 3600)
            response.set_cookie('Md5', ReadMd5(EmailAddress), max_age=7 * 24 * 3600)
            return response

        else:
            return ('验证码错误' + VerifyEmailSourceCode)
    else:
        if VerifyCode_YanZhengMa is None:
            return ('验证码错误' + VerifyEmailSourceCode)
        else:
            # print(str(verify),str(VerifyCode))
            return redirect('/signin')


@app.route('/mainpage', methods=['GET'])
def MainPage_get():
    #verify = request.cookies.get('verify')
    EmailAddress = request.cookies.get('EmailAddress')
    Md5 = request.cookies.get('Md5')
    # Preinfo='<p>欢迎您 '+EmailAddress+'<a href=/signout> 注销</a><br>'
    #if str(verify) == str(VerifyCode):
    if str(ReadMd5(EmailAddress)) == Md5:
        Preinfo = '<p>欢迎您 ' + EmailAddress + '<a href=/signout> 注销</a><br>'

        if not (ReturnEmailAddressIsVerified(EmailAddress)):
            EmailState = "<br><a href=/VerifyEmail target='_blank'> 邮箱地址未验证</a>。如学校邮箱收不到邮件，<a href=/verifybackupemail_step1 target='_blank'>点此添加并验证备用邮箱地址</a>，确保您收到通知邮件。"
        elif   not(CheckBackupEmailAddressByEmailAddress(EmailAddress)):
                EmailState="<p>您尚未设置备用邮箱地址，如学校邮箱收不到邮件，<a href=/verifybackupemail_step1 target='_blank'>点此添加并验证备用邮箱地址</a>，确保您收到通知邮件。"
        else:
            EmailState=''
        try:
            IdealAddress = (request.cookies.get('IdealAddress'))
        except:
            IdealAddress = ''
        try:
            IdealModel = (request.cookies.get('IdealModel'))
        except:
            IdealModel = ''
        if (IdealAddress is None or IdealAddress is '') and (IdealModel is None or IdealModel is ''):
            MainPageSourceCode_Now = Preinfo + EmailState + MainPageSourceCode
            for i in ReturnAllData(ReturnSexFromEmail(EmailAddress)):
                MainPageSourceCode_Now = MainPageSourceCode_Now + ' <tr>'
                for n in i:
                    MainPageSourceCode_Now = MainPageSourceCode_Now + GenerateTDHtmlSourceCode(n)
                MainPageSourceCode_Now = MainPageSourceCode_Now + ' </tr>'
            MainPageSourceCode_Now = MainPageSourceCode_Now + '</table>'
            return (MainPageSourceCode_Now)
        else:
            SearchInfo_html = '<p>搜索条件: ' + IdealAddress + ' ' + IdealModel + '<br><br>'

            if ((IdealAddress is None or IdealAddress is '') or (IdealModel is None or IdealModel is '')):
                if (IdealAddress is None or IdealAddress is ''):
                    MainPageSourceCode_Now = Preinfo + EmailState + SearchInfo_html + MainPageSourceCode
                    for i in ReturnInfoFromSexAndModel(ReturnSexFromEmail(EmailAddress), IdealModel):
                        MainPageSourceCode_Now = MainPageSourceCode_Now + ' <tr>'
                        for n in i:
                            MainPageSourceCode_Now = MainPageSourceCode_Now + GenerateTDHtmlSourceCode(n)
                        MainPageSourceCode_Now = MainPageSourceCode_Now + ' </tr>'
                    MainPageSourceCode_Now = MainPageSourceCode_Now + '</table>'
                    return (MainPageSourceCode_Now)
                else:
                    MainPageSourceCode_Now = Preinfo + EmailState + SearchInfo_html + MainPageSourceCode
                    for i in ReturnInfoFromSexAndAddress(ReturnSexFromEmail(EmailAddress), IdealAddress):
                        MainPageSourceCode_Now = MainPageSourceCode_Now + ' <tr>'
                        for n in i:
                            MainPageSourceCode_Now = MainPageSourceCode_Now + GenerateTDHtmlSourceCode(n)
                        MainPageSourceCode_Now = MainPageSourceCode_Now + ' </tr>'
                    MainPageSourceCode_Now = MainPageSourceCode_Now + '</table>'
                    return (MainPageSourceCode_Now)
            else:
                MainPageSourceCode_Now = Preinfo + EmailState + SearchInfo_html + MainPageSourceCode
                for i in ReturnInfoFromSexAndAddressAndModel(ReturnSexFromEmail(EmailAddress), IdealAddress,
                                                             IdealModel):
                    MainPageSourceCode_Now = MainPageSourceCode_Now + ' <tr>'
                    for n in i:
                        MainPageSourceCode_Now = MainPageSourceCode_Now + GenerateTDHtmlSourceCode(n)
                    MainPageSourceCode_Now = MainPageSourceCode_Now + ' </tr>'
                MainPageSourceCode_Now = MainPageSourceCode_Now + '</table>'
                return (MainPageSourceCode_Now)







    else:
        # print(ReadMd5(EmailAddress), Md5)
        response = redirect('/signin')
        response.delete_cookie('EmailAddress')
        response.delete_cookie('Md5')
        return response
    #else:
    #    return redirect('/verify')


@app.route('/mainpage', methods=['POST'])
def MainPage_post():
    print(request.form['formname'])
    if request.form['formname'] == 'Search':
        IdealAddress = str(request.form['Address'])
        IdealModel = str(request.form['Model'])
        response = redirect('/mainpage')
        response.set_cookie('IdealAddress', IdealAddress, max_age=7 * 24 * 3600)
        response.set_cookie('IdealModel', IdealModel, max_age=7 * 24 * 3600)
        return response


    elif request.form['formname'] == 'ClearSearch':
        response = redirect('/mainpage')
        response.delete_cookie('IdealAddress')
        response.delete_cookie('IdealModel')
        return response
    else:
        print('hello')


@app.route('/', methods=['GET'])
def basic_get():
    return redirect('/verify')


@app.route('/signout', methods=['GET'])
def signout_get():
    response = redirect('/signin')
    response.delete_cookie('EmailAddress')
    response.delete_cookie('Md5')
    return response


@app.route('/myinfo', methods=['GET'])
def myinfo_get():
    EmailAddress = request.cookies.get('EmailAddress')
    ReturnMyInfo = ReturnInfoFromEmailAddress(EmailAddress)
    Username = ReturnMyInfo[0]
    Sex = ReturnMyInfo[1]
    Address = ReturnMyInfo[2]
    Model = ReturnMyInfo[3]
    ContactInfo = ReturnMyInfo[4]
    Note = ReturnMyInfo[5]
    IdealAddress = ReturnMyInfo[6]
    IdealModel = ReturnMyInfo[7]
    MyDeal = ReturnMyInfo[8]
    Data = MyInfo + '<tr><td>' + Username + '</td>' + '<td>' + EmailAddress + '</td>' + '<td>' + Sex + '</td>' + '<td>' + Address + '</td>' + '<td>' + Model + '</td>' + '<td>' + ContactInfo + '</td>' + '<td>' + Note + '</td>' + '<td>' + IdealAddress + '</td>' + '<td>' + IdealModel + '</td>' + '<td>' + '' + '</td>' + '<td>' + '' + '</td>' + '<td>' + MyDeal + '</td></tr></table>'
    return Data


@app.route('/changemyinfo', methods=['GET'])
def changemyinfo_get():
    EmailAddress = request.cookies.get('EmailAddress')
    if EmailAddress=='':
        return ('/signin')
    else:
        return (ChangeMyInfoSourceCode)

@app.route('/changemyinfo', methods=['POST'])
def changemyinfo_post():
    EmailAddress = request.cookies.get('EmailAddress')
    if EmailAddress=='':
        return ('/signin')
    else:
        UserName=str(request.form['UserName'])
        ContactInfo = str(request.form['ContactInfo'])
        Address = str(request.form['Address'])
        Model = str(request.form['Model'])
        IdealAddress = str(request.form['IdealAddress'])
        IdealModel = str(request.form['IdealModel'])
        Note = str(request.form['Note'])
        #UpdateUserInfo(UserName, ContactInfo, Address, Model, IdealAddress, IdealModel, Note, EmailAddress)
        try:
            UpdateUserInfo(UserName, ContactInfo, Address, Model, IdealAddress, IdealModel, Note, EmailAddress)
            return ('更新成功<br>' + ChangeMyInfoSourceCode)
        except:
            return ('更新失败,请联系系统管理员<br>'+ChangeMyInfoSourceCode)
        #return ('更新成功<br>'+ChangeMyInfoSourceCode)

@app.route('/verifybackupemail_step1', methods=['GET'])
def VerifyBackupEmail_get():
    #verify = request.cookies.get('verify')
    EmailAddress = request.cookies.get('EmailAddress')
    # UserName = request.cookies.get('UserName')
    PreInfo = '<p> 欢迎您 ' + EmailAddress + '<br>'
    #if verify == VerifyCode:
    return (PreInfo + VerifyBackupEmailSourceCode_Step1)
    #else:
    #    return redirect('/verify')




@app.route('/verifybackupemail_step1', methods=['POST'])
def verifybackupemail_step1_post():
    EmailAddress = request.cookies.get('EmailAddress')
    BackupEmailAddress = str(request.form['BackupEmailAddress'])
    randomPort = str(random.randint(1000, 9999))
    IsVerified = str(randomPort)
    UpdateBackupEmailAddressByEmailAddress(BackupEmailAddress,EmailAddress,IsVerified)
    send_mail(BackupEmailAddress, '请验证您的备用邮箱地址', '请将验证码填入网页以验证：' + randomPort)
    return redirect('/verifybackupemail_step2')

@app.route('/verifybackupemail_step2', methods=['GET'])
def verifybackupemail_step2_get():
    EmailAddress = request.cookies.get('EmailAddress')
    EmailAddress = request.cookies.get('EmailAddress')
    # UserName = request.cookies.get('UserName')
    #PreInfo = '<p> 欢迎您 ' + EmailAddress + '<br>'
    # if verify == VerifyCode:
    return (VerifyBackupEmailSourceCode_Step2)
@app.route('/verifybackupemail_step2', methods=['POST'])
def verifybackupemail_step2_post():
    EmailAddress = request.cookies.get('EmailAddress')
    VerifyCode_YanZhengMa = str(request.form['VerifyCode'])
    if EmailAddress is not None and VerifyCode_YanZhengMa is not None:
        if CheckVerifyCode(VerifyCode_YanZhengMa, EmailAddress):
            UpdateIsVerified(EmailAddress, '1')
            return("<p>备用邮箱验证成功<br><a href='/mainpage' target='_blank'> 点此返回首页</a>")

        else:
            return ('验证码错误' + VerifyBackupEmailSourceCode)
    else:
        if VerifyCode_YanZhengMa is None:
            return ('验证码错误' + VerifyEmailSourceCode)
        else:
            # print(str(verify),str(VerifyCode))
            return redirect('/signin')





@app.route('/VerifyBackupEmail', methods=['POST'])
def VerifyBackupEmail_post():
    #verify = request.cookies.get('verify')
    EmailAddress = request.cookies.get('EmailAddress')
    VerifyCode_YanZhengMa = str(request.form['VerifyCode'])
    # print(verify,EmailAddress,VerifyCode)
    #if str(verify) == str(VerifyCode) and EmailAddress is not None and VerifyCode_YanZhengMa is not None:
    if  EmailAddress is not None and VerifyCode_YanZhengMa is not None:
        if CheckVerifyCode(VerifyCode_YanZhengMa, EmailAddress):
            UpdateIsVerified(EmailAddress, '1')
            response = redirect('/mainpage')
            response.set_cookie('EmailAddress', EmailAddress, max_age=7 * 24 * 3600)
            response.set_cookie('Md5', ReadMd5(EmailAddress), max_age=7 * 24 * 3600)
            return response

        else:
            return ('验证码错误' + VerifyBackupEmailSourceCode)
    else:
        if VerifyCode_YanZhengMa is None:
            return ('验证码错误' + VerifyEmailSourceCode)
        else:
            # print(str(verify),str(VerifyCode))
            return redirect('/signin')


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8081, debug=True,threaded=True)
