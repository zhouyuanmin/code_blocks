"""
获取疫情中高风险地区名单
http://m.bj.bendibao.com/news/gelizhengce/fengxianmingdan.php?src=baidu
"""
from urllib.request import urlopen, Request
import re


def get_epidemic_high_risk_areas():
    """获取疫情中高风险地区名单"""
    data = {"high": [], "middle": [], "status": True}
    # 获取页面
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }
    url = "http://m.bj.bendibao.com/news/gelizhengce/fengxianmingdan.php?src=baidu"
    request = Request(url, headers=header)
    try:
        res = urlopen(request)
        if res.code:
            html_bytes = res.read()
            html = html_bytes.decode()
            # 高风险
            high_pattern = "height info-item.*?middle info-item"
            high_html = re.findall(high_pattern, html, re.S)[0]
            items = re.findall('<div class="flex-between">(.*?</p>)', high_html, re.S)
            for item in items:
                province_city_list = re.findall("<span>(.*?)</span>", item, re.S)
                data["high"].append(province_city_list[0])
            # 中风险
            middle_pattern = "middle info-item.*?tiaodi info-item"
            middle_html = re.findall(middle_pattern, html, re.S)[0]
            items = re.findall('<div class="flex-between">(.*?</p>)', middle_html, re.S)
            for item in items:
                province_city_list = re.findall("<span>(.*?)</span>", item, re.S)
                data["middle"].append(province_city_list[0])
    except Exception:
        data["status"] = False
    return data


if __name__ == "__main__":
    data = get_epidemic_high_risk_areas()
    print(data)
