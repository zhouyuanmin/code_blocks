"""
获取IP现实地址
pip install qqwry-py3
"""
from qqwry import QQwry, updateQQwry
import time
import os


def get_ip_location(ip_str, data_dir=".", refresh="%Y%m"):
    """获取IP现实地址"""
    # 默认每个月更新一次dat数据
    data_file = os.path.join(
        data_dir, f"qq_wry_{time.strftime(refresh, time.localtime())}.dat"
    )
    if not os.path.isfile(data_file):
        updateQQwry(data_file)
    # 加载dat数据，并查询IP的现实地址
    q = QQwry()
    q.load_file(data_file)
    result = q.lookup(ip_str)
    return result


if __name__ == "__main__":
    result = get_ip_location("222.222.3.2", "../resources", "")
    print(result)
