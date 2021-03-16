import string
import sqlite3
import numpy as np


def extract(frist):
    second = frist[:-1].strip(')')
    third = second.strip('(')
    final = third.split(', ')
    return final


if __name__ == '__main__':
    # list = ['60', '50', '45']
    # dict = {}
    # dict['one'] = list
    #
    #
    # print (dict['one'])       # 输出键为 'one' 的值

    Sever_name = []  # 服务器名称
    Vm_name = []  # 虚拟机名称
    Sever_array = []  # 服务器数据数组
    Vm_array = []  # 虚拟机数据数组

    Vm_add = []  # 第一天add虚拟机参数
    Num = 0

    f = open(r"C:\Users\Valar Morghulis\Desktop\华为精英挑战赛\training-1.txt", "r")
    All = f.readlines()
    for frist in All:

        if frist[:-1].isdigit():
            Num += 1
            if Num == 3:
                days = int(frist[:-1])
            continue
        if Num == 1:  # 服务器数据提取
            Sever_array.append(extract(frist)[1:])
            Sever_name.append(extract(frist)[:1])
            # Sever_array = np.concatenate((Sever_array, [Final[1:]]), axis=0)

        elif Num == 2:  # 虚拟机数据提取
            Vm_array.append(extract(frist)[1:])
            Vm_name.append(extract(frist)[:1])
            # Vm_array = np.concatenate((Vm_array, [Final[1:]]), axis=0)

        elif Num == 4:  # 每天增减虚拟机数据提取
            if extract(frist)[0] == 'add':
                Vm_add.append(Vm_array[Vm_name.index([extract(frist)[1]])])

    Sever_array = np.array(Sever_array)
    Vm_array = np.array(Vm_array)
    Vm_add = np.array(Vm_add)
    # 给服务器和虚拟机数组前面标序号
    # Sever_array = np.concatenate((np.arange(0, len(Sever_array))[np.newaxis, :].T, Sever_array), axis=1)
    # Vm_array = np.concatenate((np.arange(0, len(Vm_array))[np.newaxis, :].T, Vm_array), axis=1)

    print(Vm_name[0])