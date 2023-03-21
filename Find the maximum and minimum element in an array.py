nums=[1,7,2,9,8,4,6]
min=nums[0]
max=nums[0]
for i in range(1,len(nums)):
    if nums[i]>max:
        max=nums[i]
    if nums[i]<min:
        min=nums[i]

nums.remove(max)
nums.remove(min)
print(nums)


Output:
[7, 2, 8, 4, 6]
