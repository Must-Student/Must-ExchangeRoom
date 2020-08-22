#!/usr/bin/env python3
# coding:utf-8
from flask import Flask,request,session,redirect,Response
import os
from HtmlSource import *
from DatabaseOperation import *
import random
from SendMail import *
basedir = os.path.abspath(os.path.dirname(__file__))

app =Flask(__name__)
VerifyCode='633305981'


def SendEmailToNotifyNewInfo(a,EmailAddress,UserName,Sex,Address,Model,ContactInfo,Note):
    for i in a:
        EmailAddress_NeedToSend = i[0]
        Subject='MUST-学生换租系统-您有新的可换租信息'
        Contenct='以下是新增的符合您预留的换租信息，您也可以登录https://must-student.xyz 详细查询:\n邮箱地址 用户名 性别 房租地 房型 联系信息 备注 是否已交换成功(是则显示对方邮箱地址，否显示0)\n'+ EmailAddress+' '+UserName+' '+Sex+' '+Address+' '+Model+' '+ContactInfo+' '+Note+' '+'0'
        send_mail(EmailAddress_NeedToSend,Subject,Contenct)

        print('收件人：',EmailAddress)
        print('正文：',Contenct)
    return 1


@app.route('/verify',methods=['GET'])
def verify_get():
    verify=request.cookies.get('verify')
    if verify==VerifyCode:
        return redirect('/signin')
    else:
        return (VerifySourceCode)
    
@app.route('/verify',methods=['post'])
def verify_post():
    QQGroupID=str(request.form['QQGroupID'])
    if QQGroupID ==VerifyCode:
        response = redirect('/signin')
        response.set_cookie('verify', QQGroupID, max_age=7 * 24 * 3600)
        return response
    else:
        return('QQ群号不正确，认证失败<br>'+VerifySourceCode)

@app.route('/signin',methods=['GET'])
def signin_get():
    verify=request.cookies.get('verify')
    EmailAddress = request.cookies.get('EmailAddress')
    Md5= request.cookies.get('Md5')
    if verify ==VerifyCode:
        if str(ReadMd5(EmailAddress)) == Md5:
            return redirect('/mainpage')
        else:

            return (SigninSourceCode)
    else:
        return redirect('/verify')
@app.route('/signin',methods=['post'])
def signin_post():
    verify = request.cookies.get('verify')
    if verify == VerifyCode:
        EmailAddress = str(request.form['EmailAddress'])
        PassWord = str(request.form['PassWord'])
        try:
            if CheckEmailAddressPassWord(EmailAddress,PassWord):
                response = redirect('/mainpage')
                response.set_cookie('EmailAddress', EmailAddress, max_age=7 * 24 * 3600)
                response.set_cookie('Md5', ReadMd5(EmailAddress), max_age=7 * 24 * 3600)
                print('md5:', ReadMd5(EmailAddress))
                return response
            else:
                return ('邮件地址或者密码错误' + SigninSourceCode)
        except:
            return ('邮件地址或者密码错误'+SigninSourceCode)



    else:
        return redirect('/verify')

@app.route('/signup',methods=['GET'])
def signup_get():
    verify=request.cookies.get('verify')
    EmailAddress = request.cookies.get('EmailAddress')
    Md5 = request.cookies.get('Md5')
    if verify ==VerifyCode:
        if str(ReadMd5(EmailAddress)) == Md5:
            return redirect('/mainpage')
        else:
            return (SignupSourceCode)
    else:
        return redirect('/verify')

@app.route('/signup',methods=['POST'])
def signup_post():
    verify=request.cookies.get('verify')
    if verify ==VerifyCode:
        UserName=str(request.form['UserName'])
        EmailAddress=str(request.form['EmailAddress'])
        ContactInfo=str(request.form['ContactInfo'])
        Sex=str(request.form['Sex'])
        Address=str(request.form['Address'])
        Model=str(request.form['Model'])
        IdealAddress=str(request.form['IdealAddress'])
        IdealModel=str(request.form['IdealModel'])
        Note=str(request.form['Note'])
        PassWord=str(request.form['PassWord'])
        randomPort = str(random.randint(1000, 9999))
        IsVerified=str(randomPort)
        if EmailAddress.find('@')==-1:
            EmailAddress=EmailAddress+'@student.must.edu.mo'
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

    else:
        return redirect('/VerifyEmail')

@app.route('/VerifyEmail',methods=['GET'])
def VerifyEmail_get():
    verify=request.cookies.get('verify')
    EmailAddress = request.cookies.get('EmailAddress')
    #UserName = request.cookies.get('UserName')
    PreInfo='<p> 欢迎您 '+EmailAddress+'<br>'
    if verify ==VerifyCode:
        return (PreInfo+VerifyEmailSourceCode)
    else:
        return redirect('/verify')

@app.route('/VerifyEmail',methods=['POST'])
def VerifyEmail_post():
    verify = request.cookies.get('verify')
    EmailAddress = request.cookies.get('EmailAddress')
    VerifyCode_YanZhengMa = str(request.form['VerifyCode'])
    #print(verify,EmailAddress,VerifyCode)
    if  str(verify)==str(VerifyCode) and EmailAddress is not None and VerifyCode_YanZhengMa is not None:
        if CheckVerifyCode(VerifyCode_YanZhengMa,EmailAddress):
            UpdateIsVerified(EmailAddress,'1')
            response = redirect('/mainpage')
            response.set_cookie('EmailAddress', EmailAddress, max_age=7 * 24 * 3600)
            response.set_cookie('Md5', ReadMd5(EmailAddress), max_age=7 * 24 * 3600)
            return response

        else:
            return ('验证码错误'+VerifyEmailSourceCode)
    else:
        if VerifyCode_YanZhengMa is None:
            return ('验证码错误' + VerifyEmailSourceCode)
        else:
            #print(str(verify),str(VerifyCode))
            return redirect('/verify')

@app.route('/mainpage',methods=['GET'])
def MainPage_get():
    verify=request.cookies.get('verify')
    EmailAddress= request.cookies.get('EmailAddress')
    Md5=request.cookies.get('Md5')
    Preinfo='<p>欢迎您 '+EmailAddress+'<a href=/signout> 注销</a><br>'
    if str(verify) ==str(VerifyCode):
        if str(ReadMd5(EmailAddress) )==Md5:

            if not(str(ReturnEmailAddressIsVerified(EmailAddress))=='1'):
                EmailState="<br><a href=/VerifyEmail target='_blank'> 邮箱地址未验证</a>,验证邮箱地址可确保您收到通知邮件"
            try:
                IdealAddress=(request.cookies.get('IdealAddress'))
            except:
                IdealAddress=''
            try:
                IdealModel=(request.cookies.get('IdealModel'))
            except:
                IdealModel=''
            if (IdealAddress is None or IdealAddress is '') and (IdealModel is None or IdealModel is ''):
                MainPageSourceCode_Now = Preinfo+EmailState+MainPageSourceCode
                for i in ReturnAllData(ReturnSexFromEmail(EmailAddress)):
                    MainPageSourceCode_Now = MainPageSourceCode_Now + ' <tr>'
                    for n in i:
                        MainPageSourceCode_Now = MainPageSourceCode_Now + GenerateTDHtmlSourceCode(n)
                    MainPageSourceCode_Now = MainPageSourceCode_Now + ' </tr>'
                MainPageSourceCode_Now = MainPageSourceCode_Now + '</table>'
                return (MainPageSourceCode_Now)
            else:
                SearchInfo_html='<p>搜索条件: '+IdealAddress+' '+IdealModel+'<br><br>'

                if  ((IdealAddress is  None or IdealAddress is  '') or (IdealModel is None or IdealModel is  '')):
                    if (IdealAddress is  None or IdealAddress is  ''):
                        MainPageSourceCode_Now = Preinfo+EmailState+SearchInfo_html+MainPageSourceCode
                        for i in ReturnInfoFromSexAndModel(ReturnSexFromEmail(EmailAddress), IdealModel):
                            MainPageSourceCode_Now = MainPageSourceCode_Now + ' <tr>'
                            for n in i:
                                MainPageSourceCode_Now = MainPageSourceCode_Now + GenerateTDHtmlSourceCode(n)
                            MainPageSourceCode_Now = MainPageSourceCode_Now + ' </tr>'
                        MainPageSourceCode_Now = MainPageSourceCode_Now + '</table>'
                        return (MainPageSourceCode_Now)
                    else:
                        MainPageSourceCode_Now = Preinfo+EmailState+SearchInfo_html+MainPageSourceCode
                        for i in ReturnInfoFromSexAndAddress(ReturnSexFromEmail(EmailAddress),IdealAddress):
                            MainPageSourceCode_Now = MainPageSourceCode_Now + ' <tr>'
                            for n in i:
                                MainPageSourceCode_Now = MainPageSourceCode_Now + GenerateTDHtmlSourceCode(n)
                            MainPageSourceCode_Now = MainPageSourceCode_Now + ' </tr>'
                        MainPageSourceCode_Now = MainPageSourceCode_Now + '</table>'
                        return (MainPageSourceCode_Now)
                else:
                    MainPageSourceCode_Now =Preinfo+EmailState+ SearchInfo_html+MainPageSourceCode
                    for i in ReturnInfoFromSexAndAddressAndModel(ReturnSexFromEmail(EmailAddress),IdealAddress,IdealModel):
                        MainPageSourceCode_Now = MainPageSourceCode_Now + ' <tr>'
                        for n in i:
                            MainPageSourceCode_Now = MainPageSourceCode_Now + GenerateTDHtmlSourceCode(n)
                        MainPageSourceCode_Now = MainPageSourceCode_Now + ' </tr>'
                    MainPageSourceCode_Now = MainPageSourceCode_Now + '</table>'
                    return (MainPageSourceCode_Now)







        else:
            #print(ReadMd5(EmailAddress), Md5)
            response = redirect('/signin')
            response.delete_cookie('EmailAddress')
            response.delete_cookie('Md5')
            return response
    else:
        return redirect('/verify')

@app.route('/mainpage',methods=['POST'])
def MainPage_post():
    print(request.form['formname'])
    if request.form['formname'] == 'Search':
        IdealAddress=str(request.form['Address'])
        IdealModel=str(request.form['Model'])
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

@app.route('/',methods=['GET'])
def basic_get():
    return redirect('/verify')

@app.route('/signout',methods=['GET'])
def signout_get():
    response = redirect('/signin')
    response.delete_cookie('EmailAddress')
    response.delete_cookie('Md5')
    return response



if __name__ == '__main__':

    app.run(host='127.0.0.1', port=8081, debug=False,threaded=True,ssl_context=('/etc/nginx/ssl/1_must-student.xyz_bundle.crt','/etc/nginx/ssl/2_must-student.xyz.key'))
