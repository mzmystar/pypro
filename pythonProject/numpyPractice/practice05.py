# -*- coding: UTF-8 -*-
def fun(nums1,nums2,m,n):
    nums1[m:m+n]=nums2
    nums1.sort()
    return nums1

def plusOne(digitals):
    for i in range(len(digitals)-1,0,-1):
        if digitals[i] == 9:
            digitals[i]=0
        else:
            digitals[i]+=1
            return digitals
    digitals.insert(0,1)
    return digitals
res=plusOne([9,7,7])
print(res)
