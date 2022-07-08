"""
校验身份证的18位编号的合法性
加权因子的公式是:2的18-i次幂除以11取余数,这个值即为加权因子值
"""


def get_last_value(key):
    """
    获取校验码
    @type key: int 余数,取值[0:11]
    """
    value = (12 - key) % 11
    if value == 10:
        return "X"
    else:
        return str(value)


def get_weight_factor_value(order):
    """
    获取加权因子
    @type order: int 第几位,取值[1:17]
    """
    value = 2 ** (18 - order) % 11
    return value


def check_id_card(id_card):
    """
    校验身份证编号合法性
    @type id_card: str 身份证编号
    """
    # 加权因子值 2 ** (18 - order) % 11
    weight_factor_values = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    # 校验码 (12 - key) % 11
    last_values = ["1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2"]
    # 计算最后一位编码
    nums = [int(i) for i in id_card[:-1]]
    total = 0
    for num, value in zip(nums, weight_factor_values):
        total += num * value
    last = total % 11
    last_value = last_values[last]
    # 比较
    if last_value == id_card[-1]:
        return True
    else:
        return False


if __name__ == "__main__":
    id_card_ok = "110101199003078419"
    id_card_error = "110101199003078418"
    status_ok = check_id_card(id_card_ok)
    status_error = check_id_card(id_card_error)
    print(status_ok, status_error)
