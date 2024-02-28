def lengthOfLastWord(s):
    ds_tu = s.split()
    chuoi_hop_le = " ".join(ds_tu)
    
    res = 0
    for i in range(len(chuoi_hop_le)-1, 0, -1):
        if chuoi_hop_le[i].isalpha():
            res += 1
        else:
            break
    return res
    

if __name__ == "__main__":
    s = "Hello World"
    print(lengthOfLastWord(s))