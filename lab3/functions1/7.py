def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            return True
    return False
    
a=input()
a_list=[int(nums) for nums in a.split()]
result=has_33(a_list)
print (result)