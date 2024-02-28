def removeElement(nums, val):
    j = 0
    newNums = []

    for i in range(0, len(nums)):
        if(nums[i] != val):
            nums[j] = nums[i]
            newNums.append(nums[j])
            j+=1
            
    return newNums,j

if __name__ == "__main__":
    list = [0,1,2,2,3,0,4,2]
    val = 2
    print(removeElement(list, val))

