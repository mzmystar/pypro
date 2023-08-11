# -*- coding: UTF-8 -*-
# import numpy
#
# np  = numpy.array([1,2,3,[4,5,6]],dtype=list,ndmin=2)
# dt  = numpy.dtype([('age',numpy.int8)])
# print(dt)
#
# print(np)

# 删除数组中的重复项
num = [0,1,1,2,2,3,3,3,4,4,5]
i=0
# k = len(num)
# i,j = 0,0
# while j<k:
#     if num[i]!=num[j]:
#         i=i+1
#         num[i]=num[j]
#     else:
#         j=j+1
# print(num,i,j)

def removeDuplicates(nums):
    for i in range(len(nums)-1,0,-1):
        if nums[i] == nums[i-1]:
            del num[i]
    k = len(nums)
    return k
k=removeDuplicates(num)
print(k)