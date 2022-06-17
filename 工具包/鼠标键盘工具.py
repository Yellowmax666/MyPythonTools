from pymouse import PyMouse


# 1.0 鼠标
def 点击指定坐标(positionX,positionY,clickTime=1):
    """

        :param positionX: X坐标，必须
        :type positionX: int类型

        :param positionY: Y坐标，必须
        :type positionY: int类型

        :param clickTime: 点击的次数
        :type clickTime: int类型

        .. note::

        用户指定屏幕的坐标位置，进行点击，默认点击一次

    """

    mouse = PyMouse()

    for tm in range(0,clickTime):
        mouse.click(positionX,positionY)


# 2.0 键盘
def 退格键():
    pass

def 空格键():
    pass


def 回车键():
    pass


def Table键():
    pass
