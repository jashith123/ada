import sys

sys.stdout.reconfigure(encoding='utf-8')
 
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    direction = [['']*( n+1) for _ in range(m+1)]
 
    print(f'\nString 1: "{s1}" (length {m})')
    print(f'String 2: "{s2}" (length {n})\n')
 
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                direction[i][j] = '\u2196'
            elif dp[i-1][j] >= dp[i][j-1]:
                dp[i][j] = dp[i-1][j]
                direction[i][j] = '\u2191'
            else:
                dp[i][j] = dp[i][j-1]
                direction[i][j] = '\u2190'
 
    # Print DP table with arrows
    print("DP Table (with arrows):")
    print("     |    ", end="")
    for ch in s2:
        print(f"  {ch}  ", end="")
    print()
    print("-----+" + "-----" * (n+1))
    for i in range(m+1):
        if i == 0:
            print("     |", end="")
        else:
            print(f"  {s1[i-1]}  |", end="")
        for j in range(n+1):
            if i == 0 or j == 0:
                print(f"  {dp[i][j]}  ", end="")
            else:
                print(f" {direction[i][j]}{dp[i][j]}  ", end="")
        print()
 
    # Backtrack
    lcs_chars = []
    i, j = m, n
    print(f"\nBacktracking:")
    while i > 0 and j > 0:
        if direction[i][j] == '\u2196':
            lcs_chars.append(s1[i-1])
            print(f"  [{i}][{j}]: {s1[i-1]}={s2[j-1]} \u2196 include '{s1[i-1]}', move diagonal")
            i -= 1; j -= 1
        elif direction[i][j] == '\u2191':
            print(f"  [{i}][{j}]: {s1[i-1]}!={s2[j-1]} \u2191 move up")
            i -= 1
        else:
            print(f"  [{i}][{j}]: {s1[i-1]}!={s2[j-1]} \u2190 move left")
            j -= 1
 
    lcs_chars.reverse()
    print(f'\nLCS Length: {dp[m][n]}')
    print(f'LCS String: "{"".join(lcs_chars)}"')
 
print("\n\n" + "=" * 60)
print("LCS TEST CASE 1: Classic")
print("=" * 60)
lcs("ABCBDAB", "BDCAB")
 
print("\n" + "=" * 60)
print("LCS TEST CASE 2: Different Lengths")
print("=" * 60)
lcs("AGGTAB", "GXTXAYB")
 
print("\n" + "=" * 60)
print("LCS TEST CASE 3: Identical Strings")
print("=" * 60)
lcs("ABCD", "ABCD")
 
print("\n" + "=" * 60)
print("LCS TEST CASE 4: No Common Characters")
print("=" * 60)
lcs("ABC", "XYZ")
 
print("\n" + "=" * 60)
print("LCS TEST CASE 5: PROGRAMMING vs GAMING")
print("=" * 60)
lcs("PROGRAMMING", "GAMING")
 
print("\n" + "=" * 60)
print("LCS TEST CASE 6: STONE vs LONGEST")
print("=" * 60)
lcs("STONE", "LONGEST")
 
print("\n" + "=" * 60)
print("LCS TEST CASE 7: Single Character")
print("=" * 60)
lcs("A", "A")