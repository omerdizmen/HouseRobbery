def rob(array, n, dp = {}):
    if n > len(array) - 1 or n < 0:
        return 0
    if len(array) == 1:
        return array[0]

    if n in dp:
        return dp[n]
    
    h1 = array[n]

    h1 += rob(array ,n - 2, dp)
    h2 = rob(array, n  - 1, dp)
    

    dp[n] = max(h1, h2)     
    return dp[n]

array = [6, 7, 1, 3, 8, 2, 4]
array = [5, 3, 4, 11, 2]

print(rob(array, len(array) - 1, {}))
