#!/usr/bin/env python3
# coding:utf-8
#Html SourceCode Here

def GenerateTDHtmlSourceCode(Value):
    TransferedValue='<td>'+Value+'</td>'
    return (str(TransferedValue))

VerifySourceCode="""


<script>
console.log("本站由Python Flask开发");
</script>

<!DOCTYPE html>
<html lang="cn">
<head>
    <meta charset=utf-8"utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="MUST换寝系统">
    <meta name="keyword" content="MUST换寝系统">
    <link rel="shortcut icon" href="/favicon">

    <title>MUST换寝系统-请先验证身份</title>

    <!-- Bootstrap core CSS -->
    <link href="https://simpledrive-demo.mytlu.cn/lib/view/css/bootstrap.min.css"  rel="stylesheet">
    <link href="https://simpledrive-demo.mytlu.cn/lib/view/css/bootstrap-reset.css"  rel="stylesheet">
    <!--external css-->
    <link href="https://simpledrive-demo.mytlu.cn/lib/view/assets/font-awesome/css/font-awesome.css"  rel="stylesheet" />
    <link href="https://simpledrive-demo.mytlu.cn/lib/view/assets/jquery-easy-pie-chart/jquery.easy-pie-chart.css"  rel="stylesheet" type="text/css" media="screen"/>
    <link rel="stylesheet" href="https://simpledrive-demo.mytlu.cn/lib/view/css/owl.carousel.css"  type="text/css">
    <!-- Custom styles for this template -->
    <link href="https://simpledrive-demo.mytlu.cn/lib/view/css/style.css"  rel="stylesheet">
    <link href="https://simpledrive-demo.mytlu.cn/lib/view/css/style-responsive.css"  rel="stylesheet" />
    <link href="https://simpledrive-demo.mytlu.cn/lib/view/css/index.css"  rel="stylesheet" />
    <link rel="stylesheet" type="text/css" href="https://simpledrive-demo.mytlu.cn/lib/view/assets/jquery-multi-select/css/multi-select.css"  />

</head>
<body class="loginBg">
<section id="container">
        <div class="loginLogo"></div>
        <!--sidebar start-->
        <!--sidebar end--><link href="https://simpledrive-demo.mytlu.cn/lib/view/css/login.css"  rel="stylesheet" />
    <div class="login">
        <div class="col-lg-10">
		<form action="/verify" method="post">
            <div class="input-group m-top20">
                <span class="input-group-addon"><i class="icon-user"></i></span>
                <input type="text" name="QQGroupID" id="QQGroupID" placeholder="请输入QQ群号" class="logininput form-control input-lg">
            </div>

        </div>
        <div class="col-lg-10">
            <button style="float: left;" class="btn btn-info" type="submit" id="loginbtn">验证</button>


    </div>
</section>


</body>
</html>
"""
SigninSourceCode="""



<script>
console.log("本站由Python Flask开发");
</script>

<!DOCTYPE html>
<html lang="cn">
<head>
    <meta charset=utf-8"utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="MUST换寝系统">
    <meta name="keyword" content="MUST换寝系统">
    <link rel="shortcut icon" href="/favicon">

    <title>MUST换寝系统-登录页面</title>

    <!-- Bootstrap core CSS -->
    <link href="https://simpledrive-demo.mytlu.cn/lib/view/css/bootstrap.min.css"  rel="stylesheet">
    <link href="https://simpledrive-demo.mytlu.cn/lib/view/css/bootstrap-reset.css"  rel="stylesheet">
    <!--external css-->
    <link href="https://simpledrive-demo.mytlu.cn/lib/view/assets/font-awesome/css/font-awesome.css"  rel="stylesheet" />
    <link href="https://simpledrive-demo.mytlu.cn/lib/view/assets/jquery-easy-pie-chart/jquery.easy-pie-chart.css"  rel="stylesheet" type="text/css" media="screen"/>
    <link rel="stylesheet" href="https://simpledrive-demo.mytlu.cn/lib/view/css/owl.carousel.css"  type="text/css">
    <!-- Custom styles for this template -->
    <link href="https://simpledrive-demo.mytlu.cn/lib/view/css/style.css"  rel="stylesheet">
    <link href="https://simpledrive-demo.mytlu.cn/lib/view/css/style-responsive.css"  rel="stylesheet" />
    <link href="https://simpledrive-demo.mytlu.cn/lib/view/css/index.css"  rel="stylesheet" />
    <link rel="stylesheet" type="text/css" href="https://simpledrive-demo.mytlu.cn/lib/view/assets/jquery-multi-select/css/multi-select.css"  />

</head>
<body class="loginBg">
<section id="container">
        <div class="loginLogo"></div>
        <!--sidebar start-->
        <!--sidebar end--><link href="https://simpledrive-demo.mytlu.cn/lib/view/css/login.css"  rel="stylesheet" />
    <div class="login">
        <div class="col-lg-10">
		<form action="/signin" method="post">
            <div class="input-group m-top20">
                <span class="input-group-addon"><i class="icon-user"></i></span>
                <input type="text" name="EmailAddress" id="EmailAddress" placeholder="请输入邮箱全称地址，带@" class="logininput form-control input-lg">
            </div>
            <div class="input-group m-top20">
                <span class="input-group-addon"><i class="icon-unlock-alt"></i></span>
                <input type="PassWord" name="PassWord" id="passWord" placeholder="请输入密码" class="logininput form-control input-lg">
            </div>
        </div>
        <div class="col-lg-10">
            <button style="float: left;" class="btn btn-info" type="submit" id="loginbtn">登录</button>
            <div style="float: left;margin-left: 20px;margin-top: 23px;" id="aregist">
                <label>
                    <a href='/signup'target='_blank'>还没有账号？点此注册</a>
                </label>
            </div>



    </div>
</section>


</body>
</html>

"""

SignupSourceCode="""
<form action="/signup" method="post">
<p>请输入姓名:<br>
<input type="text" name="UserName" id="UserName" placeholder="请输入用户名" class="logininput form-control input-lg">
<br>
<p>请输入学校邮箱地址（确保输入无误，稍后将发邮件验证）。邮箱地址形如12345@student.must.edu.mo,仅需输入123456即可:<br>
<input type="text" name="EmailAddress" id="EmailAddress" placeholder="请输入邮箱地址" class="logininput form-control input-lg">@student.must.edu.mo
<br>
<p>请输入联系信息（QQ/微信号/电话号码 均可）:<br>
<input type="text" name="ContactInfo" id="ContactInfo" placeholder="例：QQ10000" class="logininput form-control input-lg">
<br><p>请输入性别，可选：男/女
<p>
  <input type="text" name="Sex" id="Sex" placeholder="请输入性别" class="logininput form-control input-lg">
  <br>
<p>请输入目前宿舍地址，目前仅支持下述任意地址，请复制录入，仅可录入一地址：<br>
<p>擎天汇 海擎天 擎天半岛 国兴大厦 海明湾畔<br>
 <input type="text" name="Address" id="Address" placeholder="宿舍地址" class="logininput form-control input-lg">
<p>请输入宿舍类型字母，大写<br>
 <input type="text" name="Model" id="Model" placeholder="输入宿舍类型字母" class="logininput form-control input-lg">

 
 <p>以下填写你的意向信息：<br>
<p>请输入意向宿舍地址，可选择下述任意一个，请复制录入，也可填入0，代表不限地址：<br>
<p>擎天汇 海擎天 擎天半岛 国兴大厦 海明湾畔<br>
 <input type="text" name="IdealAddress" id="IdealAddress" placeholder="意向宿舍地址" class="logininput form-control input-lg">
<p>请输入目标宿舍类型字母，大写<br>
 <input type="text" name="IdealModel" id="IdealModel" placeholder="目标宿舍类型字母" class="logininput form-control input-lg">
 <br>
<p>请输入你想对方看到的备注信息，如请短信联系等，不想备注请输入0：<br>
 <input type="text" name="Note" id="Note" placeholder="备注信息" class="logininput form-control input-lg"><br>
<p>请设置一个登录密码，稍后系统将为您生成用户登录信息：<br>
 <input type="text" name="PassWord" id="PassWord" placeholder="输入密码" class="logininput form-control input-lg"><br>
 <br>
 <button style="float: left;" class="btn btn-info" type="submit" id="loginbtn">注册</button>
 </form>

"""
VerifyEmailSourceCode="""
<form action="/VerifyEmail" method="post">
<p>我们需要验证您的邮箱地址：<br>
<p>请输入您邮箱收到的验证码<br>
<input type="text" name="VerifyCode" id="VerifyCode" placeholder="验证码" class="logininput form-control input-lg"><br>
 <button style="float: left;" class="btn btn-info" type="submit" id="loginbtn">提交</button>
 </form>
  <br>
  <a href='/mainpage'target='_blank'>跳过认证</a>

"""
MainPageSourceCode="""
<meta http-equiv="refresh" content="30">

<form  action="/mainpage" method="post">
   <input type="hidden" style="visibility: hidden;" name="formname" value="Search" />

  <input type="text" name="Address" id="Address" placeholder="输入地址" class="logininput form-control input-lg">
  
  <input type="text" name="Model" id="Model" placeholder="输入户型" class="logininput form-control input-lg">
  
  <button   type="submit" > 搜索</button>
 </form>
 <form action="/mainpage" method="post">
 <input type="hidden" style="visibility: hidden;" name="formname" value="ClearSearch" />
<button type="submit" id="loginbtn">清除搜索信息</button>
</form>
<p><br>页面30秒自动刷新一次<br>
<p>温馨提示，您无需一直监测页面，如出现与您登记户型和地址一致的宿舍，系统将自动发邮件通知您
<br>
  
</p>
<p>房源信息：	</p>
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
	<td>是否已交换成功(是则显示对方邮箱地址，否显示0)</td>
  </tr>
  

"""
