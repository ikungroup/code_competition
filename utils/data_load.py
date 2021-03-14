import numpy as np
Array_sever = [[0, 0, 0, 0]]
Vm_sever = [[0, 0, 0]]
Num = 0

f = open(r"training-1.txt", "r")
All = f.readlines()

for frist in All:

    if Num == 1:
        if not frist[:-1].isdigit():
            second = frist[:-1].strip(')')
            third = second.strip('(')
            Final = third.split(', ')
            Array_sever = np.concatenate((Array_sever, [Final[1:]]), axis=0)
    elif Num == 2:
        if not frist[:-1].isdigit():
            second = frist[:-1].strip(')')
            third = second.strip('(')
            Final = third.split(', ')
            Vm_sever = np.concatenate((Vm_sever, [Final[1:]]), axis=0)

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
Vm_sever = np.delete(Vm_sever, 0, 0)
Array_sever = np.delete(Array_sever, 0, 0)
print(Vm_sever)
print(Array_sever)
print(Array_sever.shape)