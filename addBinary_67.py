def addBinary(s1, s2):
    if s1 == None or s1 == '0':
        return s2
    elif s2 == None or s2 == '0':
        return s1
    elif s1 == None and s2 == None:
        return "Dont' Exsit"
    else:
        res = ""
        remain = 0
        if len(s1) > len(s2):
            index = len(s1) - len(s2)
            s2 = "0" *index + s2
            for i in range(len(s1) - 1, -1 , -1):
                if(s1[i] != None or s2[i] != None):
                    if(s1[i] == s2[i] and i != 0):
                        if (s1[i] == '1' and remain == 0):
                            res += "0"
                            remain = 1
                        elif (s1[i] == '1' and remain == 1):
                            res += "1"
                            remain = 1
                        elif (s1[i] == '0' and remain == 1):
                            res += "1"
                            remain = 0
                        elif (s1[i] == '0' and remain == 0):
                            res += "0"
                        
                    elif(s1[i] != s2[i] and i != 0):
                        if(s1[i] == None and remain == 0):
                            res += s2[i]
                        elif(s1[i] == None and remain == 1):
                            if (s2[i] == "0"):
                                res += "1"
                                remain = 0
                            elif (s2[i] == "1"):
                                res += "0"
                                remain = 1
                        elif(s2[i] == None and remain == 0):
                            res += s1[i]
                        elif(s2[i] == None and remain == 1):
                            if (s1[i] == "0"):
                                res += "1"
                                remain = 0
                            elif (s1[i] == "1"):
                                res += "0"
                                remain = 1
                        elif(s1[i] == "0" and s2[i] == "1" and remain == 0):
                            res += "1"
                            remain = 0
                        elif(s1[i] == "1" and s2[i] == "0" and remain == 0):
                            res += "1"
                            remain = 0
                        elif(s1[i] == "0" and s2[i] == "1" and remain == 1):
                            res += "0"
                            remain = 1
                        elif(s1[i] == "1" and s2[i] == "0" and remain == 1):
                            res += "0"
                            remain = 1
                            
                    elif(s1[0] != s2[0]):
                        if(s1[0] == '1' and s2[0] == '0' and remain == 1):
                            res += "01"
                            remain = 0
                        elif(s1[0] == '1' and s2[0] == '0' and remain == 0):
                            res += "1"
                            remain = 0
                        if(s1[0] == '0' and s2[0] == '1' and remain == 1):
                            res += "01"
                            remain = 0
                        elif(s1[0] == '0' and s2[0] == '1' and remain == 0):
                            res += "1"
                            remain = 0
                            
        elif(len(s1) == len(s2)):
            for i in range(len(s1)-1, -1 , -1):
                if(s1[i] != None and s2[i] != None):
                    if(s1[i] == s2[i] and i != 0):
                        if (s1[i] == '1' and remain == 0):
                            res += "0"
                            remain = 1
                        elif (s1[i] == '1' and remain == 1):
                            res += "1"
                            remain = 1
                        elif (s1[i] == '0' and remain == 1):
                            res += "1"
                            remain = 0
                        elif (s1[i] == '0' and remain == 0):
                            res += "0"
                        #
                    
                    elif(s1[i] != s2[i]):
                        if(s1[i] == None and remain == 0):
                            res += s2[i]
                        elif(s1[i] == None and remain == 1):
                            if (s2[i] == "0"):
                                res += "1"
                                remain = 0
                            elif (s2[i] == "1"):
                                res += "0"
                                remain = 1
                        elif(s2[i] == None and remain == 0):
                            res += s1[i]
                        elif(s2[i] == None and remain == 1):
                            if (s1[i] == "0"):
                                res += "1"
                                remain = 0
                            elif (s1[i] == "1"):
                                res += "0"
                                remain = 1
                                
                        elif(s1[i] == "0" and s2[i] == "1" and remain == 0):
                            res += "1"
                            remain = 0
                        elif(s1[i] == "1" and s2[i] == "0" and remain == 0):
                            res += "1"
                            remain = 0
                        elif(s1[i] == "0" and s2[i] == "1" and remain == 1):
                            res += "0"
                            remain = 1
                        elif(s1[i] == "1" and s2[i] == "0" and remain == 1):
                            res += "0"
                            remain = 1
                                  
                    elif(s1[0] == s2[0]):
                        if(s1[0] == '1' and s2[0] == '1' and remain == 1):
                            res += "11"
                            remain = 0
                        elif(s1[0] == '1' and s2[0] == '1' and remain == 0):
                            res += "01"
                            remain = 0
        if len(s1) < len(s2):
            index = len(s2) - len(s1)
            s1 = "0" *index + s1
            for i in range(len(s1) - 1, -1 , -1):
                if(s1[i] != None or s2[i] != None):
                    if(s1[i] == s2[i] and i != 0):
                        if (s1[i] == '1' and remain == 0):
                            res += "0"
                            remain = 1
                        elif (s1[i] == '1' and remain == 1):
                            res += "1"
                            remain = 1
                        elif (s1[i] == '0' and remain == 1):
                            res += "1"
                            remain = 0
                        elif (s1[i] == '0' and remain == 0):
                            res += "0"
                        
                    elif(s1[i] != s2[i] and i != 0):
                        if(s1[i] == None and remain == 0):
                            res += s2[i]
                        elif(s1[i] == None and remain == 1):
                            if (s2[i] == "0"):
                                res += "1"
                                remain = 0
                            elif (s2[i] == "1"):
                                res += "0"
                                remain = 1
                        elif(s2[i] == None and remain == 0):
                            res += s1[i]
                        elif(s2[i] == None and remain == 1):
                            if (s1[i] == "0"):
                                res += "1"
                                remain = 0
                            elif (s1[i] == "1"):
                                res += "0"
                                remain = 1
                        elif(s1[i] == "0" and s2[i] == "1" and remain == 0):
                            res += "1"
                            remain = 0
                        elif(s1[i] == "1" and s2[i] == "0" and remain == 0):
                            res += "1"
                            remain = 0
                        elif(s1[i] == "0" and s2[i] == "1" and remain == 1):
                            res += "0"
                            remain = 1
                        elif(s1[i] == "1" and s2[i] == "0" and remain == 1):
                            res += "0"
                            remain = 1
                            
                    elif(s1[0] != s2[0]):
                        if(s1[0] == '1' and s2[0] == '0' and remain == 1):
                            res += "01"
                            remain = 0
                        elif(s1[0] == '1' and s2[0] == '0' and remain == 0):
                            res += "1"
                            remain = 0
                        if(s1[0] == '0' and s2[0] == '1' and remain == 1):
                            res += "01"
                            remain = 0
                        elif(s1[0] == '0' and s2[0] == '1' and remain == 0):
                            res += "1"
                            remain = 0                                                                
    return res[::-1]
        
if __name__ == "__main__":                    
    s1 = "1"
    s2 = "11"
    print(addBinary(s1,s2))

