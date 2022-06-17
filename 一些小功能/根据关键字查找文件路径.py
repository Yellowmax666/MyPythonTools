import os

def 扫描指定路径下是否包含指定关键字的文件(**kwargs):
    """

        :param key_word: 查找的关键字
        :type key_word: str

        :param search_path: 查找的路径
        :type search_path: str

        .. note::



    """


    key_word = kwargs['key_word']
    search_path = kwargs['search_path']

    # 定义非常规文件
    notNormalFiles = [".sample"]

    for dir, subdir, files in os.walk(search_path):
        # 过滤掉没有文件的目录 => []
        if len(files) != 0:
            # 拿到有文件的目录，对文件进行逐个判断
            for file in files:
                # 拿到文件，判断是否有类型
                if "." in file:
                    # 判断是否为常规文件
                    for notNormalFile in notNormalFiles:
                        if notNormalFile not in file:
                            if key_word in file:
                                print(f'找到《{key_word}》的相关文件：{os.path.join(dir,file)}')


def 根据路径获取文件大小(filePath):
    """

        :param filePath: 单个文件的路径
        :type filePath: str


        .. note::

        返回值：字节

    """

    return os.path.getsize(filePath)


if __name__ == '__main__':
    key_word = input("请输入您要查询的关键字：")
    search_path =  input("请输入您要扫描的路径（默认路径：D:/ ——>D盘全盘搜索，按下回车即可）：")
    if search_path == '':
        search_path = r'D:\飞络工作文件'
    else:
        pass

    扫描指定路径下是否包含指定关键字的文件(key_word=key_word,search_path=search_path)