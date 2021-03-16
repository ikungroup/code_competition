import numpy as np


def extract(frist):  # 将数据提取出来
    second = frist[:-1].strip(')')
    third = second.strip('(')
    final = third.split(', ')
    return final

    # list = ['60', '50', '45']
    # dict = {}
    # dict['one'] = list
    #
    #
    # print (dict['one'])       # 输出键为 'one' 的值


def read_file(file_path):
    f = open(file_path, "r")

    sever_name = []  # 服务器名称
    vm_name = []  # 虚拟机名称
    sever_array = []  # 服务器数据数组
    vm_array = []  # 虚拟机数据数组

    Vm_add = []  # 第一天add虚拟机参数
    num = 0
    All = f.readlines()
    for frist in All:

        if frist[:-1].isdigit():
            num += 1
            if num == 3:
                days = int(frist[:-1])  # 用户使用天数
            continue
        if num == 1:  # 服务器数据提取
            sever_array.append(extract(frist)[1:])
            sever_name.append(extract(frist)[:1])
            # sever_array = np.concatenate((sever_array, [Final[1:]]), axis=0)

        elif num == 2:  # 虚拟机数据提取
            vm_array.append(extract(frist)[1:])
            vm_name.append(extract(frist)[:1])
            # vm_array = np.concatenate((vm_array, [Final[1:]]), axis=0)

        elif num == 4:  # 每天增减虚拟机数据提取
            if extract(frist)[0] == 'add':
                Vm_add.append(vm_array[vm_name.index([extract(frist)[1]])])

    sever_array = np.array(sever_array)
    vm_array = np.array(vm_array)
    Vm_add = np.array(Vm_add)

    # 给服务器和虚拟机数组前面标序号
    sever_array = np.concatenate((np.arange(0, len(sever_array))[np.newaxis, :].T, sever_array), axis=1)
    vm_array = np.concatenate((np.arange(0, len(vm_array))[np.newaxis, :].T, vm_array), axis=1)

    return sever_array, vm_array


if __name__ == '__main__':
    file_path = "C:\\Users\\Valar Morghulis\\Desktop\\华为精英挑战赛\\training-1.txt"
    sever_cls, vm_cls = read_file(file_path)
    print('1')


