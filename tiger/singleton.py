"""
单例模式:函数式单例装饰器
"""


def singleton(cls):
    """函数式单例装饰器"""
    _instance = {}  # 创建一个字典用来保存被装饰类的实例对象

    def _singleton(*args, **kwargs):
        # 判断这个类有没有创建过对象，没有新创建一个，有则返回之前创建的
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton


if __name__ == "__main__":

    @singleton
    class A(object):
        def __init__(self, a=0):
            self.a = a

    a1 = A(1)
    a2 = A(2)
    print(id(a1), id(a2))  # id()函数可以获取对象的内存地址，同一内存地址即为同一对象
