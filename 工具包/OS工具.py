import pandas as pd
import os
import shutil


# 1.0 增
def 生成指定路径的文件夹(**kwargs):
    '''
    path：要创建的文件夹目录，
    :param kwargs:
    :return:True代表创建成功，False代表创建失败
    '''
    path = kwargs['path']
    if not os.path.exists(path):
        os.mkdir(path)
        return True
    else:
        return False


def 生成指定路径的文件夹tree(**kwargs):
    '''
    path：要创建的文件夹目录，
    :param kwargs:
    :return:True代表创建成功，False代表创建失败
    '''
    path = kwargs['path']
    if not os.path.exists(path):
        os.makedirs(path)
        return True
    else:
        return False

# 2.0 删
def 删除不包含指定文字的文件(**kwargs):
    '''
        saveWord：要创建的文件夹目录，
        :return:none
    '''
    saveWords = kwargs['saveWords']
    path = kwargs['path']

    for dir, subdir, files in os.walk(path):
        for filename in files:
            filepath = os.path.join(dir,filename)
            if os.path.isfile(filepath) and (saveWords[0] in filename) and (saveWords[2] in filename):
                pass
            elif os.path.isfile(filepath) and (saveWords[1] in filename) and (saveWords[2] in filename):
                pass
            else:
                os.remove(filepath)
                print(f'已删除文件------>{filename}')
                # print((saveWords[0] not in filename))
                # print((saveWords[1] not in filename))
                # print((saveWords[2] not in filename))
                # print(f'未删除文件------>{filename}')


def 删除文件夹及所有子内容(folderName):
    """

        :param folderName: 顶级文件夹路径
        :type folderName: str


        .. note::

        删除文件夹及所有子内容

    """

    shutil.rmtree(folderName)


# 3.0 改
def 判断文件夹下文件名_符合就移动至指定文件夹(**kwargs):
    '''
    fromDir：要遍历的文件夹，
    toDir：目标文件夹，
    fileContent：要判断的字符串，
    :param kwargs:
    :return:None
    '''
    fromDir = kwargs['fromDir']
    toDir = kwargs['toDir']
    fileContent = kwargs['fileContent']

    for k in os.scandir(fromDir):
        if k.is_file() and fileContent in k.name:
            shutil.move(k.path, toDir)


def 判断文件夹下文件类型并移动(**kwargs):
    '''
    fromDir：要遍历的文件夹，
    toDir：目标文件夹，
    fileContent：要判断的字符串，
    :param kwargs:
    :return:None
    '''
    fromDir = kwargs['fromDir']
    toDir = kwargs['toDir']
    fileType = kwargs['fileType']
    for k in os.scandir(fromDir):
        if k.is_file() and k.name.endswith(fileType):
            shutil.move(k.path, toDir)

# 4.0 查
def 获取指定文件夹下所有文件的绝对路径_文件有类型的(filesPath):
    """

        :param filesPath: 顶级文件夹路径
        :type filesPath: str


        .. note::

        获取指定文件夹下所有的子文件名，返回数组

    """

    # 定义非常规文件
    notNormalFiles = [".sample"]

    # 定义pathsArr，将遍历到的文件绝对目录依次添加到其中
    pathsArr = []

    for dir, subdir, files in os.walk(filesPath):
        # 过滤掉没有文件的目录 => []
        if len(files) != 0:
            # 拿到有文件的目录，对文件进行逐个判断
            for file in files:
                # 拿到文件，判断是否有类型
                if "." in file:
                    # 判断是否为常规文件
                    for notNormalFile in notNormalFiles:
                        if notNormalFile not in file:
                            pathsArr.append(os.path.join(dir,file))

    return pathsArr


def 获取指定文件夹下所有文件的名称_文件有类型的(filesPath):
    """

        :param filesPath: 顶级文件夹路径
        :type filesPath: str


        .. note::

        获取指定文件夹下所有的子文件名，返回数组

    """

    # 定义非常规文件
    notNormalFiles = [".sample"]

    # 定义pathsArr，将遍历到的文件绝对目录依次添加到其中
    pathsArr = []

    for dir, subdir, files in os.walk(filesPath):
        # 过滤掉没有文件的目录 => []
        if len(files) != 0:
            # 拿到有文件的目录，对文件进行逐个判断
            for file in files:
                # 拿到文件，判断是否有类型
                if "." in file:
                    # 判断是否为常规文件
                    for notNormalFile in notNormalFiles:
                        if notNormalFile not in file:
                            pathsArr.append(file)

    return pathsArr


def 获取指定文件夹下所有的子文件夹名(filesPath):
    """

        :param filesPath: 顶级文件夹路径
        :type filesPath: str


        .. note::

        获取指定文件夹下所有的子文件夹名，***_含指定文件夹名_***，返回数组

    """

    subDirsArr = []

    for dir, subdir, files in os.walk(filesPath):
        # 过滤掉没有文件的目录 => []
        if len(files) != 0:
            # 拿到有文件的目录，添加到数组中
            subDirsArr.append(dir)

    return subDirsArr


def 获取上级路径(path):
    """

        :param path: 路径
        :type path: str


        .. note::

        去掉指定路径的最后一个路径，比如/aaa/bbb/ccc  --> /aaa/bbb

    """

    return os.path.abspath(os.path.join(path, ".."))


def 根据路径获取文件大小(filePath):
    """

        :param filePath: 单个文件的路径
        :type filePath: str


        .. note::

        返回值：字节

    """

    return os.path.getsize(filePath)

if __name__ == '__main__':

    datas = 获取指定文件夹下所有文件的绝对路径_文件有类型的(filesPath=r'D:\飞络')

    datas_size = []
    for data in datas:
            try:
                data_size = round(根据路径获取文件大小(data)/1024/1024,3)
                datas_size.append(data_size)
            except:
                datas_size.append(0)
    # datas_size = [str(round(根据路径获取文件大小(data_size)/1024/1024,3))+"Mb"  for data_size in datas]

    print(datas)
    print(datas_size)

    a = pd.DataFrame(columns=['路径', '文件大小'])

    for indexx in range(0, len(datas_size)):
        if datas_size[indexx] > 1:
            temparr = []
            temparr.append(datas[indexx])
            temparr.append(datas_size[indexx])
            a.loc[len(a)] = temparr

    a.to_excel(r"C:\Users\huang\filesinfo.xlsx")