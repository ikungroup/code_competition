'''
使用FFD(First Fit Decreasing)解决二维装箱问题,箱子容量两个维度，箱子种类有多种，没有考虑代价和单双节点问题
ser_cls: 服务器种类，这里有ser_cls_n种 [[种类编号，CPU，内存],[种类编号，CPU，内存],...,[...]]  ser_cls_n * 3
vir_cls: 虚拟机的种类vir_cls_n种 [[物品编号，CPU，内存]，...，[...]] vie_cls_n * 3
vir_req: 虚拟机请求 [[0/1，虚拟机编号],...,[...]]  vir_req_n * 3
vir_need: 虚拟机需求 [[CPU,内存],...,[CPU，内存]] vir_need_n * 2
ser_used: 服务器的使用列表 [[编号，CPU剩余，内存剩余],...,[...]] ser_used_n*3
'''
from utils.data_load import read_file
import numpy as np
import os
np.set_printoptions(suppress=True) #不以科学计数法输出
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
bin_cls = np.array([1,32,128])
items = np.array([[1,8,12],[2,4,12],[3,32,42],[4,24,32]])
bin_cpu_cap = 32   #CPU维度的最大容量
bin_mem_cap = 128  #内存维度的最大容量


def sort_items(items):
    '''
    对物品进行排序，以物品在维度上的容量比上总容量作为重要性，最后对各个维度相加
    :param items: 待装箱的物品 [[物品编号，CPU，内存]，...，[...]]
    :return: 按照重要性程度排序后的物品 [[物品编号，CPU，内存]，...，[...]]
    '''
    scores = items.astype(np.float64)
    belta_1 = 1/sum(items[:,1:])    #用于评价物品各个维度重要性的参数
    scores[:,1:] = belta_1 * items[:,1:]
    scores[:,1:] = np.sum(scores[:,1:],axis=1,keepdims=1)
    scores = scores[:,:2]
    # scores = scores[scores[:,1].argsort()[::-1]]
    items = np.insert(items.astype(np.float64),0,np.array(scores[:,1]),axis = 1)
    items = items[items[:,0].argsort()[::-1]]
    items = np.delete(items,0,axis=1)

    return items

def sort_bins(bins):
    '''
      对箱子进行排序，以箱子在维度上的容量比上总容量作为重要性，最后对各个维度相加
    :param bins:  箱子 [[箱子种类编号，CPU，内存]，...，[...]]
    :return:  按照重要性程度排序后的箱子 [[箱子编号，CPU，内存]，...，[...]]
    '''
    scores = bins.astype(np.float64)
    belta_1 = 1 / sum(bins[:, 1:])  # 用于评价物品各个维度重要性的参数
    scores[:, 1:] = belta_1 * bins[:, 1:]
    scores[:, 1:] = np.sum(scores[:, 1:], axis=1, keepdims=1)
    scores = scores[:, :2]
    # scores = scores[scores[:,1].argsort()[::-1]]
    bins = np.insert(bins.astype(np.float64), 0, np.array(scores[:, 1]), axis=1)
    bins = bins[bins[:, 0].argsort()[::-1]]
    bins = np.delete(bins, 0, axis=1)

    return bins


def find_first_vir(vir_need,mode='max'):
    if mode == 'max':
        return vir_need[0]


def fit_sever(sever_cls,vir,cpu_lab=1,mem_lab=2):
    '''
    找到服务器列表中能够装下虚拟机的返回
    :param sever_cls: 服务器列表 [[编号，CPU，内存],...,[...]]
    :param vir: 虚拟机[编号，CPU，内存]
    :return: 返回能够装下服务器的列表 [[编号，CPU，内存],...,[...]]
    '''
    new_sever_cls = [[0,0,0]]
    for i in range(len(sever_cls)):
        if (sever_cls[i][cpu_lab] >= vir[cpu_lab]) and (sever_cls[i][mem_lab] >= vir[mem_lab]):
            new_sever_cls = np.append(new_sever_cls,np.array([sever_cls[i]]),axis=0)
    new_sever_cls = np.delete(new_sever_cls,0,axis=0)

    return new_sever_cls


def best_fit_sever(sever_cls,vir):
    '''
    在服务器列表中找到最适合虚拟机的服务器进行分配
    :param sever_cls: 服务器种类列表或者使用的服务器列表 [[编号，CPU，内存],...,[...]]
    :param vir: 需要分配的虚拟机[编号，CPU，内存]
    :return sever: 最合适的服务器 [编号，CPU，内存]
    '''
    sever_cls = fit_sever(sever_cls,vir) #首先找到能够容下服务器的列表
    scores = sever_cls
    scores[:,1:] = np.divide(vir[1:],sever_cls[:,1:])


    return sever

def assign(vir,sever,cpu_lab=1,mem_lab=2):
    '''
    对服务器分配CPU，内存，返回分配后服务器参数
    :param vir: 虚拟机 [编号，CPU，内存]
    :param sever: 服务器 [编号，CPU，内存]
    :param start: 开始进行分配的序号
    :param end: 结束分配的序号
    :return: 分配后的服务器
    '''

    sever[cpu_lab] = sever[cpu_lab] - vir[cpu_lab]
    sever[mem_lab] = sever[mem_lab] - vir[mem_lab]

    return sever



def first_assign(sever_cls,vir_need):
    vir = find_first_vir(vir_need)
    vir = vir_need[0]
    sever = best_fit_sever(sever_cls,vir)
    sever = assign(vir,sever)
    sever_used = np.array([[sever]])

    return sever_used,vir_need


def heuristic(vir_need,sever_cls,):
    #首先对虚拟机进行排序
    vir_need = sort_items(vir_need)
    sever_used,vir_need = first_assign(sever_cls,vir_need)











def pack_item(bins,item):
    '''
    对已经排好序的物品和箱子进行装箱
    :param bins: 箱子序列，格式为[[序号，物品CPU,物品内存],...,[...]]
    :param item: 待排序的物品，格式为[序号，物品CPU,物品内存]
    :return: 装箱结束后的箱子
    '''

    item_cpu,item_mem = item[1],item[2]

    for bin_num in range(len(bins)):
        bin_cpu, bin_mem = bins[bin_num][1], bins[bin_num][2]
        if (item_cpu <= bin_cpu) and (item_mem <= bin_mem):
            bins[bin_num][1], bins[bin_num][2] = bin_cpu-item_cpu,bin_mem-item_mem
            return bins

    # 原来箱子剩余容量不足以放入物品，加入新的箱子
    if (item_cpu <= bin_cpu_cap) and (item_mem <= bin_mem_cap):
        bins = np.insert(bins, 0, np.array([bin_cls]), axis=0)
        bins[0][1], bins[0][2] = bins[0][1] - item_cpu, bins[0][2] - item_mem
        return bins






if __name__ == '__main__':
    data_dir = os.path.join(BASE_DIR, "..", "data", "training-1.txt")
    vm_cls, sever_cls = read_file(data_dir)
    ONE_DAY = True
    if ONE_DAY:
        vm_cls = np.delete(vm_cls,3,axis=1)
        sever_cls = np.delete(sever_cls,3,axis=1)
        sever_cls = np.delete(sever_cls,3,axis=1)

    #获取第一天的数据



    vm_cls = sort_items(vm_cls)
    sever_cls = sort_bins(sever_cls)
    bins=ffd(bin_cls,items)