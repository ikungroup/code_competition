import numpy as np
bin = 10
items = [4,9,8,2,6]

#Best Bin Decearsing methods
def bfd(bin_cap,items):

    failure = 0
    items = sort_items(items) #sort the items
    if len(items) > 0:
        bins = [bin_cap]
    for item_num in range(len(items)):
        bf_num, bf_cap_remain = bf(bins,items[item_num])
        # 如果当前箱子内装不下物品但是全空的箱子可以，创建新的空箱子
        if (bf_num == -1) and (items[item_num] <= bin_cap):
            bins.append(bin_cap - items[item_num])
            continue
        elif (bf_num == -1): #如果没有箱子可以装下
            failure = 1
            break
        else: #如果可以装下，更新箱子容量
            bins[bf_num] = bf_cap_remain
    if failure == 1:
        raise Exception('物体体积{}大于箱子容量{}'.format(items[item_num],bin_cap))

    bins_res = np.array(bins)  #箱子剩余容量
    bins_used = bin_cap - np.array(bins)
    return bins_res,bins_used


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



def sort_items(items):

    for i in range(len(items)):
        for j in range(i+1,len(items)):
            if items[j] < items[i]:
                items[i],items[j] = items[j],items[i]
    items.reverse()
    return items
a= sort_items(items)

print(a)

bins_res,bins_used =  bfd(bin,items)
print('箱子的剩余容量',bins_res)
print('箱子已经使用容量',bins_used)