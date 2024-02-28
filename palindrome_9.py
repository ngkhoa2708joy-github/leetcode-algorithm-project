def palindrome(num):
    nums = []
    nums2 = []
    
    for i in str(num):
        nums.append(i)
        nums2 = list(nums)
    
    
    for i in range(0, len(nums)):
        if(nums2.pop() != nums[i]):
            return False
    return True
        


if __name__ == "__main__":
    num = 12121
    print(palindrome(num))