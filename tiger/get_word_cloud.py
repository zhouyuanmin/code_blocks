from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import ImageDraw, ImageFont
from io import BytesIO
import sys
import time


def get_font_path() -> str:
    if sys.platform.startswith("darwin"):
        return "/System/Library/fonts/PingFang.ttc"
    elif sys.platform.startswith("linux"):
        return "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"
    else:
        return ""


data = {
    "中专女生爆冷拿下数学竞赛全球12名": 1302923,
    "歌手发歌单了": 742696,
    "文化中国行": 689835,
    "奢香夫人": 662991,
    "美国发生大规模伤亡事件": 461934,
    "已老实 光头求放过": 393373,
    "王一博禁止擅闯车场声明": 386865,
    "歌手官宣尚雯婕袁娅维冲榜歌手": 375886,
    "LV售后欧洲免费国内收2400": 357359,
    "起底婚介公司忽悠套路": 353298,
    "王健林王思聪父子重回创富榜前十": 349538,
    "天启 家暴": 344746,
    "于正回复伊能静小作文": 340577,
    "张靓颖嘉宾 王力宏": 338941,
    "G331吉线秘境": 333237,
    "墨雨云间直播": 332614,
    "汪苏泷不会真唱奢香夫人吧": 329224,
    "手机充电一整宿有多危险": 325576,
    "日本男子被曝在多家儿童机构性侵女童": 312860,
    "京东全家桶把疯四卷疯了": 311826,
    "詹雯婷胜诉": 311592,
    "建议大家购买饮料别加冰": 311358,
    "金硕珍被亲了": 284627,
    "黄焖鸡米饭为什么不香了": 277055,
    "机场回应明星耍大牌喊旅客下电梯": 255471,
    "为什么得物越来越不受欢迎了": 253690,
    "歌手改赛制": 248756,
    "王星越为了演好萧蘅健身健疯了": 203593,
    "高三班主任花36天给每位学生写信": 175359,
    "拿到了邓超送的螺蛳粉": 171170,
    "墨雨云间男主吃烧烤蘸醋": 167816,
    "金硕珍拥抱了1000名粉丝": 162483,
    "王星越我再救你一次": 157996,
    "体检报告出现这些字眼要当心": 155572,
    "孙颖莎王楚钦入选福布斯亚洲榜": 152716,
    "张云龙回应出道多年没有火": 152372,
    "暗河传": 152366,
    "丁泽仁去当拆卡博主了": 148523,
    "张朝阳建议不用上名牌大学": 139124,
    "见过最遮光的窗帘": 136836,
    "邓超水下吐血镜头": 136801,
    "伊能静给墨雨云间写小作文": 136561,
    "双胞胎大熊猫的默契感有多强": 136116,
    "新加坡门将妻子收到打款以为诈骗": 131102,
    "江西鹰潭发生龙舟侧翻事故": 124443,
    "听说浙江人已经没地方晾衣服了": 123776,
    "鸿蒙份额超越iOS": 123684,
    "现在国外含中量有多大": 123372,
    "高考完已经急着去上大学了": 123208,
    "特斯拉股东通过马斯克天价薪酬方案": 123007,
}
mask = plt.imread("../resources/mask.jpg")

wc = WordCloud(font_path=get_font_path(), mask=mask, background_color="white", max_words=100)

wc.generate_from_frequencies(data)

img = wc.to_image()
# wc.to_file("../trash/testMask_cc12.png")

# 加水印
drawing = ImageDraw.Draw(img)
font = ImageFont.truetype(get_font_path(), 20)
text = time.strftime("微博热搜\n%Y-%m-%d %H:%M:%S", time.localtime())
color = (138, 90, 131)
pos = (50, 50)
drawing.multiline_text(pos, text, fill=color, font=font)

stream = BytesIO()
img.save(stream, format="PNG")
c = stream.getvalue()  # 将图片转为二进制数据
with open("../trash/weibo.png", "wb") as f:
    f.write(c)  # 保存到文件夹中
