def uni(nums):
    uniList = []
    for element in nums:
        if element not in uniList:
            uniList.append(element)
    return uniList

a=input()
a_list=[int(nums) for nums in a.split()]
result=uni(a_list)
print(result)