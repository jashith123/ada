def matrix_chain(dims):
    n = len(dims) - 1
    dp = [[0]*n for _ in range(n)]
    split = [[0]*n for _ in range(n)]
 
    print(f"\nMatrices: {n}")
    print(f"Dimensions: {dims}")
    for i in range(n):
        print(f"  M{i+1}({dims[i]}x{dims[i+1]})", end="")
    print("\n")
 
    for l in range(2, n+1):
        print(f"--- Chain length {l} ---")
        for i in range(n-l+1):
            j = i+l-1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + dims[i]*dims[k+1]*dims[j+1]
                better = " <-- BEST" if cost < dp[i][j] else ""
                print(f"  M{i+1}..M{j+1}, k={k+1}: {dp[i][k]}+{dp[k+1][j]}+{dims[i]}*{dims[k+1]}*{dims[j+1]}={cost}{better}")
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k
            print(f"  dp[{i}][{j}] = {dp[i][j]}\n")
 
    print("DP Table:")
    print("     ", end="")
    for j in range(n):
        print(f"{'M'+str(j+1):>8}", end="")
    print()
    for i in range(n):
        print(f"  M{i+1} |", end="")
        for j in range(n):
            if j < i:
                print(f"{'--':>8}", end="")
            else:
                print(f"{dp[i][j]:>8}", end="")
        print()
 
    print(f"\nMinimum multiplications: {dp[0][n-1]}")
    print(f"Optimal Parenthesization: {get_parens(split, 0, n-1)}")
 
def get_parens(split, i, j):
    if i == j:
        return f"M{i+1}"
    k = split[i][j]
    return f"({get_parens(split, i, k)} x {get_parens(split, k+1, j)})"
 
print("\n\n" + "=" * 60)
print("MCM TEST CASE 1: 4 Matrices")
print("=" * 60)
matrix_chain([10, 20, 30, 40, 30])
 
print("\n" + "=" * 60)
print("MCM TEST CASE 2: 3 Matrices")
print("=" * 60)
matrix_chain([40, 20, 30, 10])
 
print("\n" + "=" * 60)
print("MCM TEST CASE 3: 6 Matrices (Classic)")
print("=" * 60)
matrix_chain([30, 35, 15, 5, 10, 20, 25])
 
print("\n" + "=" * 60)
print("MCM TEST CASE 4: 3 Square Matrices")
print("=" * 60)
matrix_chain([5, 5, 5, 5])
 
print("\n" + "=" * 60)
print("MCM TEST CASE 5: 5 Matrices")
print("=" * 60)
matrix_chain([2, 3, 6, 4, 5, 3])