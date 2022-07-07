"""
获取微博热搜榜概要
https://s.weibo.com/top/summary
"""
import re
import requests


def get_weibo_hot_summary(top=10):
    """
    @type top: 0<top<=50
    """
    url = "https://s.weibo.com/top/summary"
    headers = {
        "cookie": "SUB=_2AkMVmmEbf8NxqwJRmP4QyWrka4V-ywDEieKjxpDAJRMxHRl-yj9kqk0ktRB6PhpP9FvnE1qn3Fm86OfdFRi1mfickFF_"
    }
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            pattern = '<a href=".*?Refer=top" target="_blank">(.*?)</a>.*?<span>.*? (.*?)</span>'
            hot_articles = re.findall(pattern=pattern, string=res.text, flags=re.S)[
                0:top
            ]
            return hot_articles
        else:
            return []
    except Exception:
        return []


if __name__ == "__main__":
    hot_articles = get_weibo_hot_summary(30)
    for order, hot_article in enumerate(hot_articles, 1):
        print(f"热度第{order}话题的是 #{hot_article[0]}#, 热度{hot_article[1]}")
