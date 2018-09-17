# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 23:48:41 2018

@author: zyh
顺序查找，折半查找递归和非递归算法，模式匹配
"""
# # # 顺序查找 # # #
def Search1(r,k):
    '''输入数组r，找寻数字k，返回位置，找不到则返回-1'''
    n = len(r)
    i = n-1
    while i>0:
        if r[i]==k:
            return i
        i = i-1
    return -1

# # # 非递归折半查找 # # #
def BinSearch1(r,k):
    '''非递归折半查找,输入数组r，找寻数字k，不断修改mid为上界或下界'''
    low = 0;high = len(r)-1
    while low<=high:
        mid = int((high+low)/2)  #向下取整
        if k<r[mid]:
            high = mid-1
        elif k>r[mid]:
            low = mid+1
        else:
            return mid
    return -1

# # # 递归折半查找 # # #
def BinSearch2(r,low,high,k):
    '''递归折半查找，输入数组r，找寻数字k，函数参数包含上下界，修改上下界为mid'''
    if low > high: 
        return -1
    else:
        mid = int((high+low)/2)
        if k<r[mid]:
            return BinSearch2(r,low,mid-1,k)
        elif k>r[mid]:
            return BinSearch2(r,mid+1,high,k)
        else:
            return mid

def testSearch():
    x = [1,2,4,5,6,7,9]        
    print(Search1(x,2))
    print(BinSearch1(x,2))
    print(BinSearch2(x,0,len(x)-1,2)) 
       
# # # 暴力求解子串/模式匹配 # # #
def VioSearchSubStr(a,b):
    la = len(a)
    lb = len(b)
    for i in range(la-lb+1):
        if a[i:i+lb] == b:
            return i
    return -1

def VioSearchSubStr2(a,b):
    alen = len(a)
    blen = len(b)
    i = 0;j = 0
    while i<alen:
        while a[i]==b[j]:    #逐一比较，相同且j比较完则返回，否则i,j溯回
            i += 1
            j += 1
            if j == blen:    
                return i-j
        i = i-j+1
        j = 0
    return -1

def KMPSearchSubStr(a,b):
    nex = getNext(b)
    alen = len(a)
    blen = len(b)
    i = 0;j = 0
    while i<alen:
        while a[i]==b[j]:    #逐一比较，相同且j比较完则返回，否则i,j溯回
            i += 1
            j += 1
            if j == blen:    
                return i-j
    #关键不同在于i不溯回,j进行溯回到某个点
        j = nex[j]
    return -1

def getNext(b):
    '''对b寻找前缀后缀最长公共元素长度，如abcdab最长是ab是2'''
    blen = len(b)
    nex = [0]*blen
    nex[0] = 0
    j = 1
    while j<blen:    
        #前一个nex不为0的话则比较b的对应最长子串的下一个元素是否与当前元素相同，相同则+1
        #不同则与第一个元素比较是否相同，相同则赋值为1，否则为0
        if nex[j-1]!=0 and b[nex[j-1]]==b[j]:
            nex[j] = nex[j-1]+1
        elif b[0]==b[j]:
            nex[j]=1
        else:
            nex[j]=0
        j = j+1
    return nex

#b = 'ababcabab'
#getNext(b)        
          
    
def testSearchSubStr():                
    a = 'ababcab'  
    b = 'abc'        
    print('暴力求解子串方式一：',VioSearchSubStr(a,b))
    print('暴力求解子串方式二：',VioSearchSubStr2(a,b))
    print('KMP算法求解子串：',KMPSearchSubStr(a,b))                        

if __name__ == '__main__':
    testSearch()
    testSearchSubStr()
    
    
       
