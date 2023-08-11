# -*- coding: UTF-8 -*-
# 旋转数组 python 切片功能
def fun(nums,k):
    length=len(nums)
    k = k%length
    nums[:]=nums[length-k:]+nums[:length-k]
    return nums
res =fun([1,2,3,4,5],5)
print(res)

def fun2(nums,k):
    length=len(nums)
    k = k%length
    temps=nums
    for i in range(length):
        nums[i]=temps[length-k]
    return nums
res=fun([1,2,3,4,5],5)
print(res)