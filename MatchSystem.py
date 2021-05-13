#!/usr/bin/env python3
# coding:utf-8
import pymysql
from SendMail import *
import logging
sqlservername='ServerNameHere'
sqluser='usernamehere'
sqlpasswd='passwordhere'
sqldatabase='ExchangeRoom'

HtmlCode='''
<table width="auto" border="1">
  <tr>
	<td>姓名</td>
    <td>性别</td>
    <td>地址</td>
    <td>户型</td>
	<td>联系信息</td>
	<td>备注</td>
	<td>对方期望地址（显示0为任意地址）</td>
	<td>对方期望户型（显示0为任意户型）</td>
  </tr>

'''


#PersonInfo=[[],[],[],[],[],[],[],[],[]]
#PersonInfo[0]=自己户型
#PersonInfo[1]=自己地址
#PersonInfo[2]=期待户型
#PersonInfo[3]=期待地址
#PersonInfo[4]=用户名
#PersonInfo[5]=邮箱地址
#PersonInfo[6]=备用邮箱地址
#PersonInfo[7]=性别
#PersonInfo[8]=备注

#我们这里定义三个匹配算法，三个算法具有排他性：
#1. 最优选择，匹配出100%符合你的条件的:期待户型==对方户型，对方期待户型==自己户型，自己地址==对方期待地址，对方地址==自己期待地址
#2，只匹配户型
#3，只匹配地址
#从调查问卷来看，学生对于所在地比较看重，户型次之，因此，在无100%匹配的情况下，默认先匹配地址，再匹配户型。

def SendEmail(BestMatchList,MatchModleList,MatchAddressList,myemailaddress:str,mybackupemailaddress:str,sex:str,name):
    Content=''
    if BestMatchList !=[]:
        Content=Content+'<p>为您找到完全满足条件的户型<br>' + HtmlCode
        for BestMatch in BestMatchList:
            HisModel = BestMatch[0][0]
            HisAddress = BestMatch[1][0]
            HisIdealModel = ''
            HisIdealAddress = ''
            for Model in BestMatch[2]:
                HisIdealModel = HisIdealModel + Model
            for Address in BestMatch[3]:
                HisIdealAddress = HisIdealAddress + Address
            HisName = BestMatch[4]
            HisContactInfo = BestMatch[9]
            HisNote = BestMatch[8]
            Content = Content+ '<tr><td>' + HisName + '</td><td>' + sex + '</td><td>' + HisAddress + '</td><td>' + HisModel + '</td><td>' + HisContactInfo + '</td><td>' + HisNote + '</td><td>' + HisIdealAddress + '</td><td>' + HisIdealModel + '</td> </tr>'
        Content=Content+'</table>'
    if MatchAddressList !=[]:
        Content = Content+'<br><p>为您找到满足地址条件的户型<br>' + HtmlCode
        for MatchAddress in MatchAddressList:
            HisModel = MatchAddress[0][0]
            HisAddress = MatchAddress[1][0]
            HisIdealModel = ''
            HisIdealAddress = ''
            for Model in MatchAddress[2]:
                HisIdealModel = HisIdealModel + Model
            for Address in MatchAddress[3]:
                HisIdealAddress = HisIdealAddress + Address
            HisName = MatchAddress[4]
            HisContactInfo = MatchAddress[9]
            HisNote = MatchAddress[8]
            Content = Content + '<tr><td>' + HisName + '</td><td>' + sex + '</td><td>' + HisAddress + '</td><td>' + HisModel + '</td><td>' + HisContactInfo + '</td><td>' + HisNote + '</td><td>' + HisIdealAddress + '</td><td>' + HisIdealModel + '</td> </tr>'
        Content=Content+'</table>'

    if MatchModleList !=[]:
        Content=Content+'<br><p>为您找到满足型号条件的户型<br>' + HtmlCode
        for MatchModle in MatchModleList:
            HisModel = MatchModle[0][0]
            HisAddress = MatchModle[1][0]
            HisIdealModel = ''
            HisIdealAddress = ''
            for Model in MatchModle[2]:
                HisIdealModel = HisIdealModel + Model
            for Address in MatchModle[3]:
                HisIdealAddress = HisIdealAddress + Address
            HisName = MatchModle[4]
            HisContactInfo = MatchModle[9]
            HisNote = MatchModle[8]
            Content = Content  + '<tr><td>' + HisName + '</td><td>' + sex + '</td><td>' + HisAddress + '</td><td>' + HisModel + '</td><td>' + HisContactInfo + '</td><td>' + HisNote + '</td><td>' + HisIdealAddress + '</td><td>' + HisIdealModel + '</td> </tr>'
        Content=Content+'</table>'
    Content='<p>亲爱的'+name+', 以下是满足或部分满足您换寝需求的每日报告：<br>'+Content
    if BestMatchList==[] and MatchModleList==[] and MatchAddressList==[]:
        Content=Content+'系统未匹配到任何满足您换寝需求的每日报告'
    Content=Content+'<br><p>每日报告每天早上9：00生成并发送。会生成完全匹配你需求的报告（如果存在用户匹配你）和部分匹配你需求的报告<br><p>本邮箱地址有人不定期查询回复邮件，如有问题可回邮件咨询'
    print(Content)
    print(myemailaddress,mybackupemailaddress)
    print('---------------------------------------------------')
    try:
        send_mail_html(myemailaddress, name + '-MUST-Student：换寝需求-每日报告', Content)
    except:
        print('给'+myemailaddress+'发邮件失败')
    try:
        send_mail_html(mybackupemailaddress, name + '-MUST-Student：换寝需求-每日报告', Content)
    except:
        print('给' + mybackupemailaddress + '发邮件失败')
    if BestMatchList != []:
        try:
            send_mail_html('roomexchange@must-student.xyz', '匹配成功记录-'+name + '-MUST-Student：换寝需求-每日报告', Content)
        except:
            print('给' + 'roomexchange@must-student.xyz' + '发邮件失败')
    return 1









def MatchaSystem(Data:list):

    for Me in Data:
        MactAddress = []
        MactModel = []
        BestMatchList = []
        MyEmailAddress=Me[5]
        MyBackEmailAddress=Me[6]
        for He in Data:
            for MyIdealModel in Me[2]:
                for HisIdealMode in He[2]:
                    for HisIdealAddress in He[3]:
                        for MyIdealAddress in Me[3]:
                            if ((MyIdealModel == He[0][0]) and (HisIdealMode == Me[0][0]) and (
                                    Me[1][0] == HisIdealAddress) and (
                                    He[1][0] == MyIdealAddress)):

                                BestMatchList.append(He)


                            elif (MyIdealModel==He[0][0]) :
                                MactModel.append(He)
                            elif ((MyIdealAddress==He[1][0])):

                                #Flag='3'
                                MactAddress.append(He)

        print(BestMatchList)
        SendEmail(BestMatchList,MactModel,MactAddress, MyEmailAddress, MyBackEmailAddress, Me[7],Me[4])
    return 2



def GetDataBaseData():
    db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)
    check = db.cursor()
    sql = "select * from ExchangeRoom.AccountInfo"
    check.execute(sql)
    db.commit()
    RawData=check.fetchall()
    db.close()
    return RawData

def HandleDataFromSql():
    RawData = []
    for i in (GetDataBaseData()):
        RawDataSecond = []
        for j in i:
            RawDataSecond.append(j)
        RawData.append(RawDataSecond)
    return RawData

def HandleSexData(sex:str):
    '''
    :param sex:strin，'男'或者'女'
    :return: [['B'], ['擎天半岛'], ['A'], ['擎天半岛'], '法外狂徒张三', 'qwer1gut20005@student.must.edu.mo', 'qwer1gut20005@student.must.edu.mo', '女', '', '0000291899']
    这样元素构成的数组
    '''
    RawData = HandleDataFromSql()
    SexPersonInfo = []
    for personinfo in RawData:
        if personinfo[9] == sex:
            print(personinfo)
            tempinfo = []
            tempinfo.append(personinfo[11])
            tempinfo.append(personinfo[10])
            tempinfo.append(personinfo[13])
            tempinfo.append(personinfo[12])
            tempinfo.append(personinfo[1])
            tempinfo.append(personinfo[0], )
            tempinfo.append(personinfo[15])
            tempinfo.append(sex)
            tempinfo.append(personinfo[14])
            tempinfo.append(personinfo[2])
            SexPersonInfo.append(tempinfo)
    MatchNumber = {
        'A': ['a', 'A'],
        'B': ['b', 'B'],
        'C': ['c', 'C'],
        'D': ['d', 'D'],
        'E': ['e', 'E'],
        'F': ['f', 'F'],
        'G': ['g', 'G'],
        'H': ['h', 'H'],
        'I': ['i', 'I'],
        'J': ['j', 'J'],
        'K': ['k', 'K']
    }
    RoomAddress = ['擎天汇', '海擎天', '擎天半岛', '国兴大厦', '海明湾畔']
    RawData = SexPersonInfo
    FormedRawData = []
    for EachData in RawData:
        SingleFormedRawData = []
        SelfModel = []
        SelfModel.append(EachData[0])
        SingleFormedRawData.append(SelfModel)
        SelfAddress = []
        if EachData[1] == '擎天':
            SelfAddress.append('擎天半岛')
        else:
            SelfAddress.append(EachData[1])
        SingleFormedRawData.append(SelfAddress)
        ExpectModel = []
        for Number in MatchNumber:
            # if ((MatchNumber[Number][0]==EachData[2]) or (MatchNumber[Number][1]==EachData[2])):
            if ((EachData[2].find(MatchNumber[Number][0]) > -1) or (EachData[2].find(MatchNumber[Number][1]) > -1)):
                ExpectModel.append(Number)
            elif EachData[2] == '0':
                ExpectModel.append('0')
                break
        SingleFormedRawData.append(ExpectModel)
        ExpectAddress = []
        for Room in RoomAddress:
            if (EachData[3].find(Room) > -1):
                ExpectAddress.append(Room)
            elif EachData[3] == '0':
                ExpectAddress.append('0')
                break
            elif EachData[3] == '擎天':
                ExpectAddress.append('擎天半岛')
                break
        SingleFormedRawData.append(ExpectAddress)
        SingleFormedRawData.append(EachData[4])
        SingleFormedRawData.append(EachData[5])
        SingleFormedRawData.append(EachData[6])
        SingleFormedRawData.append(EachData[7])
        SingleFormedRawData.append(EachData[8])
        SingleFormedRawData.append(EachData[9])
        FormedRawData.append(SingleFormedRawData)
    return FormedRawData

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                        level=logging.DEBUG,
                        filename='/Must-ExchangeRoom/MatchSystem.log',
                        filemode='a')
    MaleRawData=HandleSexData('男')
    FemaleRawData=HandleSexData('女')
    try:
        MatchaSystem(MaleRawData)
    except:
        print('处理男生数据失败')
    try:
        MatchaSystem(FemaleRawData)
    except:
        print('处理女生数据失败')
