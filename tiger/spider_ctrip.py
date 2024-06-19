import os
import json

from tiger.spider import base_dir, logger, create_browser

# 页面节点
page_elements = {"airport_li": '//*[@id="content"]/div/div[2]/div/div/div/div/div/div/ul/li'}


def get_airports(airports_file=""):
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


if __name__ == "__main__":
    get_airports()
