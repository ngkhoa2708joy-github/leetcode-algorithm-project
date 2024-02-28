def removeDuplicates (nums):
    j = 1
    newNums =[]
    newNums.append(nums[0])
    
    for i in range(1, len(nums)):
        if(nums[i] != nums[i-1]):
            nums[j] = nums[i]
            newNums.append(nums[j])
            j += 1
    return j, newNums

if __name__ == "__main__":
    list = [0,0,1,1,1,2,2,3,3,4]
    print(removeDuplicates(list))