import time 

def binarySearchRe(nums, target, left, right):
    if left <= right:
        mid = (right + left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return binarySearchRe(nums, target, left, mid - 1)
        elif nums[mid] < target:
            return binarySearchRe(nums, target, mid + 1, right)
    else:
        return "Dont'exist"
    
def searchLoop(nums, target):
    for i in range(0,len(nums)):
        if(nums[i] == target):
            return i
    return "Dont't exsit"

if __name__ == "__main__":
    nums = [0,1,2,3,4,7,9,12,15,24,100,102,103,200,450,1234,1300,9000,12000]
    target = 103
    
    print("Array: ", nums)
    
    
    start_time1 = time.perf_counter()
    res1 = binarySearchRe(nums, target, 0, len(nums)-1)
    end_time1 = time.perf_counter()
    
    start_time2 = time.perf_counter()
    res2 = searchLoop(nums, target)
    end_time2 = time.perf_counter()
    
    
    
    duration1 = (end_time1 - start_time1)*1000
    duration2 = (end_time2 - start_time2)*1000
    
    print("=>(BINARY SEARCH) Found the target value at index:", res1, "after {:.5f} milliseconds" .format(duration1))
    print("=>(LOOP) Found the target value at index:", res2, "after {:.5f} milliseconds" .format(duration2))


# O(log(n))