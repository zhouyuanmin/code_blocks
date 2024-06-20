import os
import json
import time
from selenium.common.exceptions import UnexpectedAlertPresentException
from spider import base_dir, logger, create_browser

# 页面节点
page_elements = {
    "airport_li": '//*[@id="content"]/div/div[2]/div/div/div/div/div/div/ul/li',
    "textbox": '//*[@id="sou_suo_value"]',
    "button": '//*[@id="api_map_top"]/input[2]',
    "lng_show": '//*[@id="all_lng_show"]',
    "lat_show": '//*[@id="all_lat_show"]',
}


def get_airports(airports_file=""):
    """爬取携程，获取基本的机场信息，有266个机场"""
    if not airports_file:
        airports_file = os.path.join(base_dir, "trash", "airports.json")

    browser = create_browser()
    url = "https://flights.ctrip.com/booking/airport-guides.html"
    browser.get(url)
    airport_lis = browser.find_elements_by_xpath(page_elements.get("airport_li"))
    airports = {}
    for li in airport_lis:
        city, airport = li.text.split("\n")
        airport_url = li.find_element_by_tag_name("a").get_attribute("href")
        airport_code = airport_url.split("-")[-1]
        airports[airport] = {"city": city, "airport": airport, "airport_url": airport_url, "airport_code": airport_code}

    with open(airports_file, "w") as f:
        content = json.dumps(airports, ensure_ascii=False)
        f.write(content)
    browser.quit()
    logger.info(f"抓取完成，共{len(airports)}个机场")


def add_gps(airports_file=""):
    """经纬度查询，给机场加上gps信息"""
    if not airports_file:
        airports_file = os.path.join(base_dir, "trash", "airports.json")

    # 读取JSON文件的数据
    with open(airports_file, "r") as file:
        airports = json.load(file)

    browser = create_browser()
    url = "https://jingweidu.bmcx.com/"
    browser.get(url)
    count = 5
    for i, k in enumerate(airports, start=1):
        if airports[k].get("lng", ""):
            continue
        if count <= 0:
            time.sleep(300)
            count = 5
        else:
            count -= 1
        try:
            textbox = browser.find_element_by_xpath(page_elements.get("textbox"))
            textbox.clear()
            textbox.send_keys(k)
            button = browser.find_element_by_xpath(page_elements.get("button"))
            button.click()
            time.sleep(10)
            lng_show = browser.find_element_by_xpath(page_elements.get("lng_show"))
            lng = lng_show.get_attribute("value")
            lat_show = browser.find_element_by_xpath(page_elements.get("lat_show"))
            lat = lat_show.get_attribute("value")
            airports[k]["lng"] = lng
            airports[k]["lat"] = lat
            logger.info(f"{i}:{json.dumps(airports[k], ensure_ascii=False)}")
        except UnexpectedAlertPresentException as e:
            logger.warning(e)
            time.sleep(600)
            continue
        except Exception as e:
            logger.error(e)
        finally:
            with open(airports_file, "w") as f:
                content = json.dumps(airports, ensure_ascii=False)
                f.write(content)
    browser.quit()
    logger.info(f"抓取完成，共更新{len(airports)}个机场")


def check_gps(airports_file=""):
    """检查gps并删除脏数据"""
    if not airports_file:
        airports_file = os.path.join(base_dir, "trash", "airports.json")
    # 读取JSON文件的数据
    with open(airports_file, "r") as file:
        airports = json.load(file)
    lng_set = set()
    lng_set.add("104.48060937499996")  # 默认的北京GPS
    status = True
    for i, k in enumerate(airports, start=1):
        lng = airports[k].get("lng", "")
        if not lng:
            status = False
            continue
        if lng in lng_set:
            status = False
            airports[k].pop("lng")
            airports[k].pop("lat")
    with open(airports_file, "w") as f:
        content = json.dumps(airports, ensure_ascii=False)
        f.write(content)

    return status


if __name__ == "__main__":
    # get_airports()
    # add_gps()
    # check_gps()
    pass
