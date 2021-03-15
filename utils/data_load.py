import numpy as np


def read_file(file_path):
    f = open(file_path, "r")
    sever_cls = [[0, 0, 0, 0]]
    vm_cls = [[0, 0, 0]]
    Num = 0
    All = f.readlines()
    for frist in All:

        if Num == 1:
            if not frist[:-1].isdigit():
                second = frist[:-1].strip(')')
                third = second.strip('(')
                Final = third.split(', ')
                sever_cls = np.concatenate((sever_cls, [Final[1:]]), axis=0)
        elif Num == 2:
            if not frist[:-1].isdigit():
                second = frist[:-1].strip(')')
                third = second.strip('(')
                Final = third.split(', ')
                vm_cls = np.concatenate((vm_cls, [Final[1:]]), axis=0)

        elif Num == 3:
            all_day = int(frist[:-1])
            # 剩下的是每天的增删操作
        if frist[:-1].isdigit():  # 下一行判断
            Num += 1

    # second = frist[:-1].strip(')')
    # third = second.strip('(')
    # Final = third.split(', ')
    # New.append(Final)
    # Array_sever.append(np.array(Final[1:]))

    vm_cls = np.delete(vm_cls, 0, 0)
    sever_cls = np.delete(sever_cls, 0, 0)

    #转化为整数，添加类别列
    sever_cls = sever_cls.astype('int')
    server_num = [x for x in range(len(sever_cls))]
    sever_cls = np.insert(sever_cls, 0, server_num, 1)
    # sever_cls = sever_cls.astype('int')

    vm_cls = vm_cls.astype(int)
    vm_num = [[x for x in range(len(vm_cls))]]
    vm_cls = np.insert(vm_cls, 0, vm_num, axis=1)
    return vm_cls,sever_cls

if __name__ == '__main__':
    file_path = "C:\\Users\\王连兴\\Desktop\\competition\\data\\training-1.txt"
    vm_cls,sever_cls = read_file(file_path)
   
    a=2

