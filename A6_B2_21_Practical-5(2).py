def lrs(S):
    n = len(S)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    direction = [[''] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if S[i - 1] == S[j - 1] and i != j:
                dp[i][j] = dp[i - 1][j - 1] + 1
                direction[i][j] = 'match'
            elif dp[i - 1][j] >= dp[i][j - 1]:
                dp[i][j] = dp[i - 1][j]
                direction[i][j] = 'up'
            else:
                dp[i][j] = dp[i][j - 1]
                direction[i][j] = 'left'

    i, j = n, n
    lrs_str = []
    while i > 0 and j > 0:
        if direction[i][j] == 'match':
            lrs_str.append(S[i - 1])
            i -= 1
            j -= 1
        elif direction[i][j] == 'up':
            i -= 1
        else:
            j -= 1

    print("Length of LRS:", dp[n][n])
    print("LRS:", ''.join(reversed(lrs_str)))


S = "AABCBDC"
lrs(S)
