import io
import sys

_INPUT = """\
6
2 19
2 3
5 6
2 18
2 3
5 6
3 1001
1 1
2 1
100 10
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,X=map(int,input().split())
  dp=[0]*(10**4+1)
  dp[0]=1
  for i in range(N):
    A,B=map(int,input().split())
    for j in reversed(range(10**4+1)):
      if dp[j]==1:
        for k in range(B):
          if j+(k+1)*A<=10**4: dp[j+(k+1)*A]=1
  if dp[X]==1: print('Yes')
  else: print('No')