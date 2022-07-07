"""
获取不同尺寸的QQ头像
尺寸有: 40,100,140,640
"""
import requests


def get_qq_avatar(qq_number, size=100):
    base_url = "https://q4.qlogo.cn/g?b=qq&nk=%s&s=%s"
    url = base_url % (qq_number, size)
    try:
        res = requests.get(url)
        if res.status_code == 200:
            return {"status": True, "content": res.content}
        else:
            return {"status": False, "content": ""}
    except requests.RequestException:
        return {"status": False, "content": ""}


if __name__ == "__main__":
    data = get_qq_avatar("1837722596", 640)
    if data.get("status"):
        with open("../trash/qq_avatar.png", "wb+") as f:
            f.write(data.get("content"))
    else:
        print(data)
