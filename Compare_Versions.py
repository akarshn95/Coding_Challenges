def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        l = min(len(v1), len(v2))
        
        flag = True
        i = 0
        for i in range(l):
            if int(v1[i]) != int(v2[i]):
                flag = False
            
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
            
        if flag:
            if len(v1) > len(v2):
                for j in v1[l:]:
                    if int(j)!=0:
                        return 1
                return 0
            elif len(v1) == len(v2):
                return 0
            else:
                for j in v2[l:]:
                    if int(j)!=0:
                        return -1
                return 0
