def spy_game(nums):
    spyNum = [0, 0, 7]
    i = 0 #индекс
    for num in nums:
        if num == spyNum[i]:
            i += 1
            if i == len(spyNum):
                return True
    return False
a=input()
a_list=[int(nums) for nums in a.split()]
result=spy_game(a_list)
print(result)