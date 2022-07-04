"""
第三方认证登录:QQ登陆
需要安装第三方包: pip install QQLoginTool
由于QQLoginTool是为django实现的QQ登录工具,所以需要安装Django,不限制Django版本
"""
from QQLoginTool.QQtool import OAuthQQ

# QQ登录参数
QQ_CLIENT_ID = "101949193"
QQ_CLIENT_SECRET = "b8d6a2628706b589fd5d3701bf9896ca"
QQ_REDIRECT_URI = "https://www.myard.cn/oauth_callback.html"

# 获取QQ登录页面网址
oauth = OAuthQQ(
    client_id=QQ_CLIENT_ID,
    client_secret=QQ_CLIENT_SECRET,
    redirect_uri=QQ_REDIRECT_URI,
    state="index.html",
)
login_url = oauth.get_qq_url()
print(login_url)  # 将链接粘贴到浏览器请求，登陆成功之后，返回的链接就包含了code的值

code = "88CA442E5A36478F664FABABC1AFCC42"
if code:
    # 通过code获取access_token
    access_token = oauth.get_access_token(code)
    print(access_token)
    # 通过access_token获取openid
    openid = oauth.get_open_id(access_token)
    print(openid)
