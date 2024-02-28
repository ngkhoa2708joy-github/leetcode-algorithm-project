def sqrt_x(x, left, right):
    while (left <= right):
        mid = (right + left) // 2
        if mid * mid > x: # mid > x / mid (overflow in other languages)
            right = mid - 1
        elif mid * mid < x: # mid < x / mid
            left = mid + 1
        else: 
            return mid
    return right

if __name__ == "__main__":
    x = 64
    nums = [i for i in range(0,x+1)]
    left = 0
    right = len(nums)
    print(sqrt_x(x, left, right))