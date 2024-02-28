def plusOne(s):
    s[len(s)-1] = s[len(s)-1] + 1
    res_1 = s[len(s)-1]
    if res_1 >= 10:
        s.pop()
        for i in str(res_1):
            s.append(int(i)) 
    return s

if __name__ == "__main__":
    s = [4,3,2,9]
    print(plusOne(s))
    