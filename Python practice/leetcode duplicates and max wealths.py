# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 15:18:22 2021

@author: Test
"""

#%%
#duplicates
class Solution:
    def containsDuplicate(self, numbers):
        if len(set(numbers))==len(numbers):
            return False
        else:
            return True

a=[1,2,3,1]
b=[1,2,3,4]
c=[1,1,1,3,3,4,3,2,4,2]

ans = Solution()
print(ans.containsDuplicate(a))

#%%


#Max Wealths
class Solution:
       
    def max_wealth(self,accounts):  
        maximum = 0
        for element in accounts:
             maximum = max(sum(element),maximum)
        return maximum
    
x=[[1,2],[2,3]]
u=[[1,5],[7,3],[3,5]]
y=[[1,2,3],[3,2,1]]
z=[[2,8,7],[7,1,3],[1,9,5]]

ans = Solution()
a=ans.max_wealth(x)
print(a)

#%% 
#running sum of 1d array
a=[1,2,3,4]
b=[1,1,1,1,1]
c=[3,1,2,10,1]
class solution:
    def runningsum(self,array):
        ans = []
        sum =0
        for i in array:
            sum = sum + i
            ans.append(sum)
        return ans

ans = solution()
print(ans.runningsum(c))

#%%
#kids with candies
a=[2,3,5,1,3]
b=[4,2,1,1,2]
c=[12,1,12]
class solution:
    
    def candies(self, num,extras):
        result = []
        for i in num:
            candy = i + extras
            greatest = candy >= max(num)
            result.append(greatest)
        return result

ans = solution()
print(ans.candies(b,2))

#%%
#Check If Two String Arrays are Equivalent
class solution:
    def equalarrays(self, str1, str2):
        s1=''
        s2=''
        for i in str1:
            s1+=i
        for j in str2:
            s2+=j
        return(s1==s2)

a=["ab", "c"]
b=["a", "bc"]
c=["a", "cb"]
d=["ab", "c"]
e=["abc", "d", "defg"]
f=["abcddefg"]       

ans=solution()
print(ans.equalarrays(e,f))

#%%
#sqrt

def sqrt(num):
    x=0
    while x*x<=num:
        x+=1
    return x-1

print(sqrt(1000))

#%%
class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.car=[big,medium,small]
        
    def addCar(self, carType: int) -> bool:
        self.car[carType-1] -=1
        return self.car[carType-1]>=0
    
a=ParkingSystem(1,1,0)
print(a.addCar(1))
print(a.addCar(2))
print(a.addCar(3))
print(a.addCar(1))

#%% shuffle
class Solution:
    def shuffle(self, nums):
        n=len(nums)//2
        arr1=nums[:n]
        arr2=nums[n:]
        x=[]
        for i in range(n):
            x.append(arr1[i])
            x.append(arr2[i])
        return x
        
a=[2,5,1,3,4,7]
b=[1,2,3,4,4,3,2,1]
c=[1,1,2,2]
d=[1,2,3,4,5,1,2,3,4,5]
print(len(a)//2)

ans=Solution()
print(ans.shuffle(a))
print(ans.shuffle(b))
print(ans.shuffle(c)) 
print(ans.shuffle(d)) 

#%% shuffle string
class Solution:
    def shuffstring(self,s,indices):
        soln=[""]*len(s)
        for i in range(len(s)):
            soln[int(indices[i])]=s[i]
        soln="".join(soln) #must be out of for loop
        return soln



a = "codeleet" 
b = [4,5,6,7,0,2,1,3]     

c="abc"
d=[0,1,2]

e="aiohn"
f=[3,1,4,2,0]

g="aaiougrt"
h=  [4,0,2,6,7,3,1,5]

ans=Solution()
print(ans.shuffstring(a,b))
print(ans.shuffstring(c,d))
print(ans.shuffstring(e,f))
print(ans.shuffstring(g,h))

#%% even digits
class Solution:
    def evendigits(self,nums):
        x=0
        for element in nums:
           if len(str(element))%2==0:
               x+=1
        return x
        
        
a = [12,345,2,6,7896]
b=[555,901,482,1771]
ans=Solution()
print(ans.evendigits(a))
print(ans.evendigits(b))

#%% Two Sum
print("two sum")
nums = [2,7,11,15] 
target = 18
# nums = [3,2,4] 
# target = 6
#   brute force
#  def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i,j]
#     return False

def twoSum(nums, target):
    dictN = {}
    for index, value in enumerate(nums):
        remaining = target - nums[index]
        if remaining in dictN:
            return [index, dictN[remaining]]
        dictN[value] = index



ans = twoSum(nums, target)
print(ans)
# %% Best time to buy and sell stock

x = [7,1,5,3,6,4]
y = [1,2,3,4,5]
z = [7,6,4,3,1]

def maxProfit(arr):
    buy = False
    i = 0
    j = 0
    profit = 0
    while i < len(arr):
        if not buy:
            while i+1 < len(arr) and arr[i] >= arr[i+1]:
                i += 1
            j = i+1
            buy = True
            if j > len(arr) - 1:
                break
        else:
            while j+1 < len(arr) and arr[j] < arr[j+1]:
                j+=1
            profit = profit + arr[j] - arr[i]
            i = j
            buy = False
    return profit

print(maxProfit(x))
print(maxProfit(y))
print(maxProfit(z))



# %%
