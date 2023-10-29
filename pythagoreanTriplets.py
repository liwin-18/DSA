def checkTriplet(self, arr, n):
        square_set = set()
        for num in arr:
            square_set.add(num * num)
        
        for i in range(n - 1):
            for j in range(i + 1, n):
                if (arr[i] * arr[i] + arr[j] * arr[j]) in square_set:
                    return True
        return False
# tc: O(n^2), sc: O(n)