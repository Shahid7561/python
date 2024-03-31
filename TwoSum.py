def twoSum(nums,target):
    num_indices = {}  # Hash map to store encountered numbers and their indices

    for i, num in enumerate(nums):
        complement = target - num
            
        # If the complement is already in the hash map, return the indices
        if complement in num_indices:
            return [num_indices[complement], i]
            
        # Otherwise, add the current number and its index to the hash map
        num_indices[num] = i
        
        # If no solution is found, return an empty list
    return []
nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))