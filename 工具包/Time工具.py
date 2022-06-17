import pandas as pd
import os
import shutil
import time

def 获取当天日期_不含时间(timeStrType=1):
    """

        :param timeStrType: 格式的形式
        :type timeStrType: int

        .. note::

        type为1：返回的格式为："%Y年%m月%d"

        type为2：返回的格式为："%Y-%m-%d"

        type为2：返回的格式为："%Y_%m_%d"

    """
    if timeStrType == 1:
        return time.strftime("%Y年%m月%d日", time.localtime(time.time()))
    elif timeStrType == 2:
        return time.strftime("%Y-%m-%d", time.localtime(time.time()))
    elif timeStrType == 3:
        return time.strftime("%H_%M_%S", time.localtime(time.time()))


def 获取当前时间_不含日期(timeStrType=1):
    """

        :param timeStrType: 格式的形式
        :type timeStrType: int

        .. note::

        type为1：返回的格式为："%H:%M:%S"

        type为2：返回的格式为："%H-%M-%S"

        type为2：返回的格式为："%H_%M_%S"

    """
    if timeStrType == 1:
        return time.strftime("%H:%M:%S", time.localtime(time.time()))
    elif timeStrType == 2:
        return time.strftime("%H-%M-%S", time.localtime(time.time()))
    elif timeStrType == 3:
        return time.strftime("%H_%M_%S", time.localtime(time.time()))


def 获取当天日期及时分秒(timeStrType=1):
    """

        :param timeStrType: 格式的形式
        :type timeStrType: int

        .. note::

        type为1：返回的格式为："%Y-%m-%d %H:%M:%S"

        type为2：返回的格式为："%Y-%m-%d %H-%M-%S"

        type为3：返回的格式为："%Y_%m_%d_%H_%M_%S"

    """
    if timeStrType == 1:
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    elif timeStrType == 2:
        return time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    elif timeStrType == 3:
        return time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime(time.time()))


def 获取时间差(timeStart:time.struct_time,timeEnd:time.struct_time):
    """

        :param timeStart: 开始的时间
        :type timeStart: time.localtime(time.time())

        :param timeEnd: 结束的时间
        :type timeEnd: time.localtime(time.time())

        .. note::

        根据传入的两个**time.localtime(time.time())**对象，计算它们之间的时间差

    """

    HourPass = timeEnd.tm_hour - timeStart.tm_hour
    MinPass = timeEnd.tm_min - timeStart.tm_min
    SecondPass = timeEnd.tm_sec - timeStart.tm_sec
    conca = str(HourPass) + "小时" + str(MinPass) + "分" + str(SecondPass) + "秒"
    return conca

def 睡眠(sleepTime=1):
    """

        :param sleepTime: 睡眠时长
        :type sleepTime: int类型

        .. note::

        使程序暂停执行，默认值为1秒

    """

    time.sleep(sleepTime)