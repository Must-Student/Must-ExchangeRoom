# Must-ExchangeRoon
A System used for Exchange the Room.
<br><br>
Requirement:

Python3, Flask, MySql
<br>
<br>
Use ExchangeRoom.sql to create Mysql database.
<br>
<br>
In Order TO Generate A Report To All User, pls add the following crontab info to your Linux Server.<br>
 For details see man 4 crontabs
<br>
 Example of job definition:<br>
 .---------------- minute (0 - 59)<br>
 |  .------------- hour (0 - 23)<br>
 |  |  .---------- day of month (1 - 31)<br>
 |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...<br>
 |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat<br>
 |  |  |  |  |<br>
 *  *  *  *  * user-name  command to be executed<br>
0 9 * * * root /Must-ExchangeRoom/MatchSystem.py<br>
<br>
Must换寝系统，使用ExchangeRoom.sql生成数据库。本程序基于Python Flask，使用前请安装pymysql，flask等模块，安装Python3。<br>
新增生成每日换寝信息匹配报告系统，为了系统正常运行，请在Linux Crontab里添加如下任务。<br>

<br>
<br>
 Example of job definition:<br>
 .---------------- minute (0 - 59)<br>
 |  .------------- hour (0 - 23)<br>
 |  |  .---------- day of month (1 - 31)<br>
 |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...<br>
 |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat<br>
 |  |  |  |  |<br>
 *  *  *  *  * user-name  command to be executed<br>
0 9 * * * root /Must-ExchangeRoom/MatchSystem.py<br>
<br>

