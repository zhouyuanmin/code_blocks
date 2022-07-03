"""
使用容联云通讯平台来发送短信验证码
需要安装sdk库: pip install ronglian-sms-sdk
"""
from ronglian_sms_sdk import SmsSDK
import json


def send_message(acc_id, acc_token, app_id):
    sdk = SmsSDK(acc_id, acc_token, app_id)
    tid = "1"
    mobile = "17859717522"
    data = (1234, 5)
    res = sdk.sendMessage(tid, mobile, data)
    if json.loads(res).get("statusCode") == "000000":
        return True
    return False


if __name__ == "__main__":
    acc_id = "8a216da8762cb4570176ef87f32243ba"
    acc_token = "97f09583668147a8ad064c9d139f408a"
    app_id = "8a216da8762cb4570176ef87f42243c1"
    result = send_message(acc_id, acc_token, app_id)
    print(result)
