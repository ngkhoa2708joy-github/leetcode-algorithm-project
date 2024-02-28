def searchInsertPosion(nums, val):
    for i in range(0, len(nums)):
        if nums[i] == val:
            return i    
        elif val > nums[len(nums)-1]:
          return len(nums) 
        else:   
            if val > nums[i] and val < nums[i+1]:
                return i + 1
            elif val < nums[0]:
                return 0
    return -1

if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 7
    print(searchInsertPosion(nums, target))