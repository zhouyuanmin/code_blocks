"""
URL长链接转短链接
https://www.mxnzp.com/doc/detail?id=26
"""
import base64
import requests


def long2short(long_url, only_code=False):
    """长链接转短链接"""
    url = "https://www.mxnzp.com/api/shortlink/create"
    params = {
        "url": base64.urlsafe_b64encode(long_url.encode()),
        "app_id": "lkxoyzovyhmcmshj",
        "app_secret": "NnNWZFArcHRtdDdxMnJra0I0Z1dGZz09",
    }
    try:
        res = requests.get(url, params=params)
        data = res.json()
        if data.get("code") == 1:
            short_url = data.get("data").get("shortUrl")
            if only_code:
                return short_url[-4:]
            else:
                return short_url
        else:
            return ""
    except Exception:
        return ""


if __name__ == "__main__":
    long_url = "https://www.baidu.com/"
    short_url = long2short(long_url=long_url)
    print(short_url)
