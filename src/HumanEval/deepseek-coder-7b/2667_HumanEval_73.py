
def smallest_change(arr):
    n = len(arr)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # Initialize dp table for single characters
    for i in range(n):
        dp[i][i] = 1

    # Fill dp table for lengths of 2
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            dp[i][i+1] = 2
        else:
            dp[i][i+1] = 1

    # Fill dp table for lengths greater than 2
    for length in range(3, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if arr[i] == arr[j]:
                dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    # The minimum number of changes is n - LPS
    return n - dp[0][n-1]

