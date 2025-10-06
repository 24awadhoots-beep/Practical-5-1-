def lcs(X, Y):
    m, n = len(X), len(Y)

    dp = [[0] * (n + 1) for _ in range(m + 1)]
    direction = [[''] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                direction[i][j] = 'match'
            elif dp[i - 1][j] >= dp[i][j - 1]:
                dp[i][j] = dp[i - 1][j]
                direction[i][j] = 'up'
            else:
                dp[i][j] = dp[i][j - 1]
                direction[i][j] = 'left'

    i, j = m, n
    lcs_str = []
    while i > 0 and j > 0:
        if direction[i][j] == 'match':
            lcs_str.append(X[i - 1])
            i -= 1
            j -= 1
        elif direction[i][j] == 'up':
            i -= 1
        else:
            j -= 1

    print("Cost Matrix (LCS Lengths):")
    for row in dp:
        print(row)

    print("\nDirection Matrix:")
    for row in direction:
        print(' '.join(row))

    print("\nLength of LCS:", dp[m][n])
    print("LCS:", ''.join(reversed(lcs_str)))


X = "AGCCCTAAGGGCTACCTAGCTT"
Y = "GACAGCCTACAAGCGTTAGCTTG"

lcs(X, Y)
