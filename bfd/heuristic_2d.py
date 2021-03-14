'''
使用FFD(First Fit Decreasing)解决二维装箱问题,箱子容量两个维度，箱子种类只有一种
bin_cls: 箱子种类，这里只有一种 [种类编号，CPU，内存]
items: 待装箱的物品 [[物品编号，CPU，内存]，...，[...]]
'''



import numpy as np
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

# def sort_bins(bins):
#     '''
#       对箱子进行排序，以箱子在维度上的容量比上总容量作为重要性，最后对各个维度相加
#     :param bins:  箱子 [[箱子种类编号，CPU，内存]，...，[...]]
#     :return:  按照重要性程度排序后的箱子 [[箱子编号，CPU，内存]，...，[...]]
#     '''
#     scores = bins.astype(np.float64)
#     belta_1 = 1 / sum(bins[:, 1:])  # 用于评价物品各个维度重要性的参数
#     scores[:, 1:] = belta_1 * bins[:, 1:]
#     scores[:, 1:] = np.sum(scores[:, 1:], axis=1, keepdims=1)
#     scores = scores[:, :2]
#     # scores = scores[scores[:,1].argsort()[::-1]]
#     items = np.insert(bins.astype(np.float64), 0, np.array(scores[:, 1]), axis=1)
#     items = items[items[:, 0].argsort()[::-1]]
#     items = np.delete(items, 0, axis=1)
#
#     return bins


#First Fit Decearsing methods
def ffd(bin_cls,items):


    items = sort_items(items) #sort the items
    if len(items) > 0:
        bins = np.array([bin_cls])
    # bins = sort_bins(bins)  因为只有一种箱子，所以不需要排序
    for item_num in range(len(items)):
        # for bins_num in range(len(bins)):
        bins = pack_item(bins,items[item_num])
    return bins





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
    bins=ffd(bin_cls,items)
