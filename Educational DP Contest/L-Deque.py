import sys
import collections
from math import ceil, gcd, sqrt, log
import bisect

INF = float('inf')
mod = 1000000007

# Bottom Up Approach
# Filling DP table for smaller subarrays first, increasing order (subarray length 1, 2, 3...)

def solve():
    n = int(input())
    A = list(map(int, input().split()))

    DP = [[0] * (n + 1) for i in range(n + 1)]

    for i in range(n):
        DP[i][i] = A[i]
    
    for d in range(1, n):
        for i in range(n - d):
            j = i + d
            DP[i][j] = max(A[i] - DP[i + 1][j], A[j] - DP[i][j - 1])
    

    print(DP[0][n - 1])
    


t = 1

while t != 0:
    solve()

    t -= 1
    