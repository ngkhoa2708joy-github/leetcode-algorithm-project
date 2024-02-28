def findFirstIndexOfOccurrence(s1, s2):
    if len(s2) > len(s1):
        return -1
    for i in range(0, len(s1)):
        if s1[i:i + len(s2)] == s2:
            return i
    return -1

if __name__ == "__main__":
    s1 = "hellovietnamnumber1"
    s2 = "ber1"
    print(findFirstIndexOfOccurrence(s1,s2))