def histogram(nums):
    for i in nums:
        print("*"*i)

a=input()
a_list=[int(nums) for nums in a.split()]
result=histogram(a_list)
print(result)

