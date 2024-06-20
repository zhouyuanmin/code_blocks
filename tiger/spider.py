from selenium import webdriver
from pathlib import Path
import logging
import random
import time
import sys
import os

# 全局配置信息
base_dir = Path(__file__).resolve().parent.parent
proxy = "http://127.0.0.1:4780"
window_width, window_height = (1250, 900)  # 需要根据分辨率来确定窗口大小

# 日志配置
logging.basicConfig(level=logging.INFO, format="%(asctime)s - line:%(lineno)d - %(levelname)s: %(message)s")
log_path = os.path.join(base_dir, "logs", "client.log")
file_handler = logging.FileHandler(log_path)
file_handler.setFormatter(logging.Formatter("%(asctime)s - line:%(lineno)d - %(levelname)s: %(message)s", "%Y-%m-%d %H:%M:%S"))
file_handler.setLevel(logging.INFO)

logger = logging.getLogger(__name__)
logger.addHandler(file_handler)

# 页面节点
page_elements = {}


# 基础函数
def waiting_to_load(browser, count=10, sleep_time=1):
    """等待页面加载"""
    if sleep_time:
        time.sleep(sleep_time)
    while True:
        status = browser.execute_script("return document.readyState")
        if status == "complete":
            return True
        elif count <= 0:
            return False
        else:
            time.sleep(0.5)
            count -= 1


def scroll_to_bottom(browser, count=None):
    """滚动页面,到页面底部"""
    js = "return action=document.body.scrollHeight"
    height = 0
    new_height = browser.execute_script(js)

    while height < new_height:
        for i in range(height, new_height, 100):
            browser.execute_script("window.scrollTo(0, {})".format(i))
            time.sleep(0.5)
        browser.execute_script("window.scrollTo(0, {})".format(new_height - 1))
        height = new_height
        time.sleep(1)
        new_height = browser.execute_script(js)
        if count is None:
            continue
        else:
            count -= 1
            if count < 0:
                return False
    return True


def get_driver():
    if sys.platform.startswith("win32"):
        driver = os.path.join(base_dir, "resources", "chromedriver.exe")
    elif sys.platform.startswith("darwin"):
        driver = os.path.join(base_dir, "resources", "chromedriver")
    else:
        logger.error("不支持此类操作系统")
        sys.exit(0)
    return driver


def create_browser(tm_proxy="", is_proxy=True):
    """
    创建browser
    index: 0 默认使用第一个代理
    """
    global window_width
    global window_height
    global proxy
    if not tm_proxy:
        tm_proxy = proxy
    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values": {"notifications": 1}}
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--ignore-certificate-errors")
    if is_proxy:
        options.add_argument(f"--proxy-server={tm_proxy}")

    driver = get_driver()
    browser = webdriver.Chrome(driver, options=options)
    x, y = random.randint(10, 30), random.randint(10, 30)
    browser.set_window_rect(x, y, width=window_width, height=window_height)
    return browser


if __name__ == "__main__":
    print(base_dir)
    print(get_driver())
