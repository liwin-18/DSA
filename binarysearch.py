def searchInSorted(self,arr, N, K):
	l=0
        u=N-1
        while(l<=u):
            m=(l+u)//2
            if(arr[m]==K):
                return 1
            elif(arr[m]>K):
                u=m-1
            else:
                l=m+1
        return -1