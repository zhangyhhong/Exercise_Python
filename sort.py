# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 18:31:16 2018

@author: zyh
"""
# # # 插入排序1：直接插入排序 # # #
'''
最优时间复杂度：O(n) 基本有序
最坏时间复杂度：O(n2)
稳定
'''
def InsertSort(x):
    n = len(x)
    for i in range(1,n):
        for j in range(i,0,-1):
            if x[j]<x[j-1]:    #与前面的比较，若是比前面的小则交换顺序
                x[j],x[j-1] = x[j-1],x[j]
            else:
                break
    return x

def InsertSort2(x):
    n = len(x)
    for i in range(1,n):
        k = i-1
        xx = x.pop(i)   #对该元素，找到要插入的位置，直接插入
        while xx<x[k] and k>1:  
            k = k-1
        x.insert(k+1,xx)
    return x

# # # 插入排序2：希尔排序 # # #
'''对整个序列分成若干个子序列，对子序列分别进行插入排序'''
def ShellSort(x):
    n = len(x)
    d = n//2
    while d>=1:    #不通过间隔有不同的子序列
        for i in range(d,n):
            for j in range(i,d-1,-d):
                if x[j]<x[j-d]:    #与前面的第d个比较，若是比前面的小则交换顺序
                    x[j],x[j-d] = x[j-d],x[j]
                else:
                    break
        d = d//2
    return x

# # # 交换排序1：冒泡排序算法 # # # 
def BubbleSort(x):
    nlen = len(x)
    for i in range(nlen-1,0,-1):
        for j in range(0,i):
            if x[j]>x[j+1]:
                x[j],x[j+1] = x[j+1],x[j]
    return x

# # # 交换排序2：快速排序算法 # # # 
def Partition(x,i,j):
    '''一次划分算法'''
    while i<j:
        while i<j and x[i]<=x[j]:   #右侧扫描
            j = j-1            
        if i<j:    #不满足x[i]<=x[j]时，调换i，j位置
            x[i],x[j] = x[j],x[i]
            i = i+1
       
        while i<j and x[i]<=x[j]:   #左侧扫描
            i = i+1
        if i<j:    #不满足x[i]<=x[j]时，调换i，j位置
            x[i],x[j] = x[j],x[i]
            j = j-1
    return i

def QuickSort(x,i,j):    #递归无返回
    if i<j:
        p = Partition(x,i,j)
        QuickSort(x,i,p-1)
        QuickSort(x,p+1,j)

# # # 选择排序1：简单选择排序算法 # # #      
def SimSeleSort(x):
    xlen = len(x)
    for i in range(xlen):
        mi = x[i]
        t = i
        for j in range(i,xlen):            
            if x[j]<mi :
                mi = x[j]
                t = j
        x[i],x[t] = x[t],x[i]
    return x
# # # 选择排序2：堆排序 # # # 
def AdjustHeap(x,i,size):   #筛选，得到一个位置i，将x[i]加入到堆中
    lchild = 2*i+1
    rchild = 2*i+2
    ma = i
    if i<size/2:
        if lchild<size and x[lchild]>x[ma]:
            ma = lchild
        if rchild<size and x[rchild]>x[ma]:
            ma = rchild
        if ma != i:
            x[ma],x[i] = x[i],x[ma]
            AdjustHeap(x,ma,size)
            
def BuildHeap(x,size):  #建堆就是不断进行筛选的过程
    for i in range(0,size//2)[::-1]:
        AdjustHeap(x,i,size)
        
def HeapSort(x):
    size = len(x)        
    BuildHeap(x,size)
    for i in range(0,size)[::-1]:
        x[0],x[i] = x[i],x[0]   #x[0]是堆顶
        AdjustHeap(x,0,i)
        
            
    
# # # 二路归并排序 # # # 
def Merge(x,y):    #一次归并算法
    xlen = len(x)
    ylen = len(y)
    z = []
    i = 0; j = 0
    while i<xlen and j<ylen:
        if x[i] <= y[j]:
            z.append(x[i])
            i = i+1
        else:
            z.append(y[j])
            j = j+1
    if i<xlen:
        z.extend(x[i:])
    else:
        z.extend(y[j:])
    return z
#Merge([1,3,5],[2,4,7,8,9])

def MergeSort(x):
    if len(x)<=1:
        return x    
    mid = len(x)//2
    l = MergeSort(x[:mid])
    r = MergeSort(x[mid:])
    return Merge(l,r)

# # # 分配排序1：桶式排序 # # # 
def BucketSortNum(x):   #对整数进行排序，适合多重复的整数
    xmin = min(x)
    xmax = max(x)
    bucket = [0]*(xmax-xmin+1)  #桶的数量取决于x跨度
    for i in x:
        bucket[i-xmin] += 1
    res = []
    for i in range(len(bucket)):
        res.extend([i+xmin]*bucket[i])
    return res

# # # 分配排序2：桶式排序 # # # 
def RadixSort(x):
    d = len(str(max(x)))    #位数    
    b = [[] for _ in range(10)]
    for i in x:    
        dd = i%10   #个位数
        b[dd].append(i)
    x = sum(b,[])    
    for k in range(2,d+1):
        b = [[] for _ in range(10)]
        for i in x:
            dd = i%10**k//10**(k-1)   #取各个位数上的数字,取千位，除以1000取余数再整除100
            b[dd].append(i)
        x = sum(b,[])
    return x



# # # 测试算法 # # # 
def test():
    x = [1,4,3,8,5,9,0] 
    print('排序前：',x)       
    print('直接插入排序后：',InsertSort(x))
    print('希尔排序后：',ShellSort(x))
    print('冒泡排序法：',BubbleSort(x))
    print('简单选择排序：',SimSeleSort(x))
    HeapSort(x)
    print('堆排序：')   #无返回
    x = [1,4,3,8,5,9,0]
    print('归并排序：',MergeSort(x))
    
    y = [12,34,567,234,5689,4325]
    print('基数排序',RadixSort(y))
    QuickSort(x,0,len(x)-1)   #无返回
    print('快排后：',x)


if __name__ == '__main__':
    test()
    
