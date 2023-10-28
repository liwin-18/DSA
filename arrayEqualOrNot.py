def check(self,A,B,N):
        mp={}
        for i in range(N):
            if A[i] in mp.keys():
                mp[A[i]]+=1
            else:
                mp[A[i]]=1
        for j in range(N):
            if B[j] not in mp.keys():
                return 0
            mp[B[j]]-=1
        for i in mp.keys():
            if mp[i]!=0:
                return 0
        return 1
        