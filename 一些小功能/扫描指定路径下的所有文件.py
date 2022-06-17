import pandas as pd
import os

def 获取指定文件夹下所有文件的绝对路径_文件有类型的(filesPath):
    """

        :param filesPath: 顶级文件夹路径
        :type filesPath: str


        .. note::

        获取指定文件夹下所有的子文件名，返回数组

    """

    # 定义非常规文件
    notNormalFiles = [".sample"]

    # 定义pathsArr，将遍历到的文件绝对目录依次添加到其中notNormalFiles
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

def 根据路径获取文件大小(filePath):
    """

        :param filePath: 单个文件的路径
        :type filePath: str


        .. note::

        返回值：字节

    """

    return os.path.getsize(filePath)


if __name__ == '__main__':
    scan_field = input("请输入您要扫描的路径（如：C: ——> 代表扫描C盘所有）：")
    below_size = int(input("请输入您要获取大于多少M的文件？（如：10 ——> 代表获取大于10MB的文件）："))
    to_file = input("请输入您要保存的Excel文件的路径（如：C:\my_files.xlsx ——> 代表保存为C:\my_files.xlsx这个文件，注：文件会自动创建）：")
    datas = 获取指定文件夹下所有文件的绝对路径_文件有类型的(filesPath=scan_field)

    datas_size = []
    for data in datas:
        try:
            data_size = round(根据路径获取文件大小(data ) /1024 /1024 ,3)
            datas_size.append(data_size)
        except:
            datas_size.append(0)

    print(datas)
    print(datas_size)

    a = pd.DataFrame(columns=['路径', '文件大小(MB)'])

    for indexx in range(0, len(datas_size)):
        if datas_size[indexx] > below_size:
            temparr = []
            temparr.append(datas[indexx])
            temparr.append(datas_size[indexx])
            a.loc[len(a)] = temparr

    a.to_excel(to_file)