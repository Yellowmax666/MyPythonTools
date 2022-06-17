import pandas as pd
import os
import json





# 1.0 操作列

def 保留指定的列(**kwargs):
    '''
        saveColumns：要保留的列，类型：数组，
        data：Dataframe数据，
        :param kwargs:
        :return:newdata
    '''
    saveColumns = kwargs['saveColumns']
    data = kwargs['data']

    # 1.如果用户传入的saveColumns不是数组类型，报错
    if type(saveColumns) != list:
        raise Exception('传入的saveColumns数据不是数组类型')

    allColumns = list(data.columns)

    # 从allColumns中删除要保存的列名
    for saveColumnName in saveColumns:
        allColumns.remove(saveColumnName)

    return data.drop(allColumns, axis=1)


def 删除指定的列(**kwargs):
    '''
    data：数据，
    delColumns：要删除的列，类型为列表，
    :param kwargs:
    :return:newdata
    '''
    delColumns = kwargs['delColumns']
    data = kwargs['data']
    return data.drop(delColumns,axis=1)


def 重命名指定的列(**kwargs):
    '''
    data：DataFrame数据，
    originalColumnName：原列名，
    newColumnName：修改目标列名，
    :param kwargs:None
    :return:None
    '''

    data = kwargs['data']
    originalColumnName = kwargs['originalColumnName']
    newColumnName = kwargs['newColumnName']

    data.rename(columns={originalColumnName: newColumnName}, inplace="true")


def 改变列的位置(**kwargs):
    '''
    :param kwargs:
    postion:要放到的位置，
    data：数据，
    column：要改变的字段
    :return:
    '''
    position = kwargs['postion'] - 1
    data = kwargs['data']
    column = kwargs['column']
    dropField = data[column]
    filedLen = len(list(data.keys()))
    # 判断用户输入的长度是否超出指定范围
    if int(position)+1 > int(filedLen):
        data = "超出长度，请重新输入column！"
    else:
        data.drop(column, axis=1, inplace="truell")
        data.insert(position, column, dropField)
    return data

def 将指定列转换为数组(data,col):
    """

        :param data: Dataframe数据，
        :type data: dataframe

        :param col: 列名，类型为string
        :type col: str

        .. note::

        将指定列转换为数组

    """

    # col需要转换为list，才能调用保留指定的列函数，使用split可以将其转换为数组
    col = col.split("........")

    data = 保留指定的列(saveColumns=col,data=data)
    colArr = [data[0] for data in data.values]

    return colArr


# 2.0 操作行
def 删除整行都是空值的(**kwargs):
    '''
         data：Dataframe数据，
         :param kwargs:
         :return:newdata
     '''

    kwargs['data'].dropna(how='all', inplace="truell")
    return kwargs['data']


def 判断指定的列_为空就删除行(**kwargs):
    '''
         data：Dataframe数据，
         ColArr：要判断是否为空的列，类型为数组，
         :param kwargs:
         :return:newdata
     '''

    data = kwargs['data']
    colArr = kwargs['colArr']

    data.dropna(axis=0, subset = colArr,inplace="truell")

    return data


def 对行分组_并用指定连接符连接其他数据(**kwargs):
    '''
        data：Dataframe数据，
        groupBy：分组源列，
        groupDataSource：分组数据列，
        connector：连接符，
        :param kwargs:
        :return:newdata
    '''

    data = kwargs['data']
    groupBy = kwargs['groupBy']
    groupDataSource = kwargs['groupDataSource']
    connector = kwargs['connector']

    data = data.groupby(groupBy)[groupDataSource].agg(connector.join)

    return data


def 判断指定列_若该列该有特定字符就删除整行(**kwargs):
    '''
        data：Dataframe数据，
        col：要判断的列，
        content：要判断的内容，如果包含该内容，就删除，
        :param kwargs:
        :return:newdata
    '''
    data = kwargs['data']
    col = kwargs['col']
    content = kwargs['content']

    newData = data[~data[col].isin([content])]

    return newData


def 判断指定列_若该列该有特定字符就保留整行_删除其他所有行(**kwargs):
    '''
        data：Dataframe数据，
        col：要判断的列，
        content：要判断的内容，如果包含该内容，就保留，若无，就删除，
        :param kwargs:
        :return:newdata
    '''
    data = kwargs['data']
    col = kwargs['col']
    content = kwargs['content']

    newData = data[data[col].isin([content])]

    return newData



# 3.0 对整个Dataframe的操作

def 转置表(**kwargs):
    '''
    data：Dataframe数据，
    :param kwargs:
    :return:
    '''
    data = kwargs['data']
    data = pd.DataFrame(data.values.T,index=data.columns,columns=data.index)
    return data


def 过滤指定的数据(**kwargs):
    kwargs['data'].query(kwargs['conditions'],inplace="truell")
    return kwargs['data']

def 分组聚合(**kwargs):
    '''
    所需参数：
    groupField，
    groupMethods，
    data
    axis → 可选
    method → 可选
    '''
    groupField = kwargs['groupField']
    groupMethods = kwargs['groupMethods']
    data = kwargs['data']
    if 'axis' not in kwargs:
        # 按列进行分组
        data = data.groupby(groupField).agg(groupMethods)
    else:
        # 按行进行分组
        data = f'请按照data.groupby(groupMethods,axis=1).sum()的方式自行书写'
    return data


# 4.0 逐行处理

def 根据映射条件新增列_并且该列的内容为映射的值(**kwargs):
    '''
    data：数据，
    mapDic：映射条件字典，
    OFiled：被映射的字段，
    NField：映射出的字段
    :return:
    '''

    data = kwargs['data']
    mapDic = kwargs['mapDic']
    OFiled = kwargs['OFiled']
    NField = kwargs['NField']

    data[NField] = data[OFiled].map(mapDic)

    return data


# 5.0 跨Dataframe处理
def 左查询两个Dataframe(**kwargs):
    '''
    lQueryData：左查询的Dataframe，
    infoData：被查询的左查询的Dataframe，
    queryField：左查询所用的字段，
    :return:finalData，合并查询后的数据
    '''

    lQueryData = kwargs['lQueryData']
    infoData = kwargs['infoData']
    queryField = kwargs['queryField']

    finalData = pd.merge(lQueryData,infoData,on=queryField,how='left')

    return finalData


def 右查询两个Dataframe(**kwargs):
    '''
    lQueryData：右查询的Dataframe，
    infoData：被查询的右查询的Dataframe，
    queryField：右查询所用的字段，
    :return:finalData，合并查询后的数据
    '''

    lQueryData = kwargs['lQueryData']
    infoData = kwargs['infoData']
    queryField = kwargs['queryField']

    finalData = pd.merge(lQueryData,infoData,on=queryField,how='right')

    return finalData

# 6.0 其他文件格式处理
def JSON转Dataframe(**kwargs):
    '''
    jsonFilePath：json文件的路径，
    queryField：右查询所用的字段，
    :return:data，jsonStr转Dataframe后的数据
    '''
    jsonFilePath = kwargs['jsonFilePath']
    data = pd.read_json(jsonFilePath)

    return data


if __name__ == '__main__':
    pass
