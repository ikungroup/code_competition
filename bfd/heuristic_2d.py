'''
二维装箱问题
'''


#箱子容量两个维度，箱子种类只有一种的装箱问题
import numpy as np
bin_cls = np.array([1,32,128])
items = np.array([[1,8,12],[2,4,12],[3,32,42]])
bin_cpu_cap = 32
bin_mem_cap = 128


def sort_items(items):
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
    scores = bins.astype(np.float64)
    belta_1 = 1 / sum(bins[:, 1:])  # 用于评价物品各个维度重要性的参数
    scores[:, 1:] = belta_1 * bins[:, 1:]
    scores[:, 1:] = np.sum(scores[:, 1:], axis=1, keepdims=1)
    scores = scores[:, :2]
    # scores = scores[scores[:,1].argsort()[::-1]]
    items = np.insert(bins.astype(np.float64), 0, np.array(scores[:, 1]), axis=1)
    items = items[items[:, 0].argsort()[::-1]]
    items = np.delete(items, 0, axis=1)

    return bins
#Best Bin Decearsing methods
def bfd(bin_cls,items):

    failure = 0
    items = sort_items(items) #sort the items
    if len(items) > 0:
        bins = np.array([bin_cls])
    bins = sort_bins(bins)
    for item_num in range(len(items)):
        # for bins_num in range(len(bins)):
        bins = pack_item(bins,items[item_num])



    #     bf_num, bf_cap_remain = bf(bins,items[item_num])
    #     # 如果当前箱子内装不下物品但是全空的箱子可以，创建新的空箱子
    #     if (bf_num == -1) and (items[item_num] <=bin_cap):
    #         bins.append(bin_cap - items[item_num])
    #         continue
    #     elif (bf_num == -1): #如果没有箱子可以装下
    #         failure = 1
    #         break
    #     else: #如果可以装下，更新箱子容量
    #         bins[bf_num] = bf_cap_remain
    # if failure == 1:
    #     raise Exception('物体体积{}大于箱子容量{}'.format(items[item_num],bin_cap))
    #
    # bins_res = np.array(bins)  #箱子剩余容量
    # bins_used = bin_cap - np.array(bins)
    # return bins_res,bins_used

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


bfd(bin_cls,items)





#找到装物品之后使得剩余容量最小的箱子
def bf(bin_cap,item):
    bf_cap_remain = 1e10
    bf_num = -1
    for i in range(len(bin_cap)):
        if ((bin_cap[i] - item) >= 0):
            cap_remain = bin_cap[i] - item
            if(cap_remain<bf_cap_remain):
                bf_cap_remain = cap_remain
                bf_num = i
    return bf_num,bf_cap_remain

bin_cap = [10,6,4,5,3]
bf_num,bf_cap_remain = bf(bin_cap,11)
o=2





a= sort_items(items)

print(a)

bins_res,bins_used =  bfd(bin,items)
print('箱子的剩余容量',bins_res)
print('箱子已经使用容量',bins_used)