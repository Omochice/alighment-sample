def levenshtein(str1: str,
                str2: str,
                show_table: bool = True,
                show_alignment: bool = True) -> int:
    # compute
    dp = [[0] * (len(str1) + 1) for _ in range(len(str2) + 1)]
    for i in range(len(str1) + 1):
        dp[0][i] = i
    for i in range(len(str2) + 1):
        dp[i][0] = i
    for j in range(1, len(str2) + 1):
        for i in range(1, len(str1) + 1):
            cost = int(not str1[i - 1] == str2[j - 1])
            dp[j][i] = min(dp[j - 1][i] + 1, dp[j][i - 1] + 1, dp[j - 1][i - 1] + cost)

    # show table
    if show_table:
        print([" ", " "] + list(str1))
        tmp = " " + str2
        for i, row in enumerate(dp):
            print([tmp[i]] + list(map(str, row)))

    # show matching
    if show_alignment:
        i = len(dp[0]) - 1
        j = len(dp) - 1
        matcher = ""
        while not (i == 0 and j == 0):
            window = []
            if i == 0:
                window.append(float("inf"))
            else:
                window.append(dp[j][i - 1])
            if i == 0 or j == 0:
                window.append(float("inf"))
            else:
                window.append(dp[j - 1][i - 1])
            if j == 0:
                window.append(float("inf"))
            else:
                window.append(dp[j - 1][i])
            mindex = window.index(min(window))
            if mindex == 0:    # left
                str2 = str2[:j] + "-" + str2[j:]
                i = i - 1
                matcher += " "
            elif mindex == 1:    # left up
                i = i - 1
                j = j - 1
                matcher += "|"
            else:    # up
                str1 = str1[:i] + "-" + str1[i:]
                j = j - 1
                matcher += " "
        print(str1)
        print(matcher[::-1])
        print(str2)

    return dp[-1][-1]


if __name__ == "__main__":
    # levenshtein("DOROTHYHODGKIN", "DOROTHYCROWFOOTHODGKIN")
    levenshtein("agtcc", "cgctca")
