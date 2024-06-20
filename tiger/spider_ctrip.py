import os
import json
import time
from selenium.common.exceptions import UnexpectedAlertPresentException
from tiger.spider import base_dir, logger, create_browser

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


def add_gps(old_airports_file="", new_airports_file=""):
    """经纬度查询，给机场加上gps信息"""
    if not old_airports_file:
        old_airports_file = os.path.join(base_dir, "resources", "airports.json")
    if not new_airports_file:
        new_airports_file = os.path.join(base_dir, "trash", "airports.json")

    # 读取JSON文件的数据
    with open(old_airports_file, "r") as file:
        airports = json.load(file)

    browser = create_browser()
    url = "https://jingweidu.bmcx.com/"
    browser.get(url)
    for i, k in enumerate(airports, start=1):
        if airports[k].get("lng", ""):
            continue
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
            time.sleep(660)
            continue
        except Exception as e:
            logger.error(e)
        finally:
            with open(new_airports_file, "w") as f:
                content = json.dumps(airports, ensure_ascii=False)
                f.write(content)
    browser.quit()
    logger.info(f"抓取完成，共更新{len(airports)}个机场")


if __name__ == "__main__":
    # get_airports()
    add_gps()
