"""
JWT认证 Authorization
需要在headers里面构建一个字段Authorization
内容是 JWT + 空格 + jwt内容
"""
import requests

headers = {
    "Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkI-oxLCJ1c2Vy-mFtZSI6IjE3ODU5NzE3NTIyIi-iZXhwIj-xNjEyNDAyMDU1LCJlbWFpbCI6IiJ9.1ILI1-AdAb8InFVwwVovLu7mH1W2qM9FY-DJplDPwhI",
}  # 注意JTW后面跟了一个空格
a = requests.get(url="https://httpbin.org/get", headers=headers)
print(a.json())
