"""
本地化时间
解决django orm操作时间遇到的警告问题
"""
from datetime import datetime
from pytz import timezone

now_time = datetime.now()
time_zone = timezone("Asia/Shanghai")
localize_time = time_zone.localize(now_time)
print(localize_time)
print(now_time.tzinfo is not None)
print(localize_time.tzinfo is not None)
