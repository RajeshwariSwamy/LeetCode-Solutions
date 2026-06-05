class Solution(object):
    def twoSum(self, nums, target):
        output = []
        x=len(nums)
        for i in range(0, len(nums)):
            #print(i)   
            c=i
            while c<x-1:
              #print(i, c)     
              if (nums[i] + nums[c+1] == target):
                  #print(nums[i],nums[c+1], x)
                  output.extend([i, c+1])            
                  #output.append(i)
                  #output.append(c+1)
                  return output
                  #break
              c+=1       
            if len(output) > 0:
              break

    



    






"""
:type nums: List[int]
:type target: int
:rtype: List[int]
"""
        