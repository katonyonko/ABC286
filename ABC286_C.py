import io
import sys

_INPUT = """\
6
5 1 2
rrefa
8 1000000000 1000000000
bcdfcgaa
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,A,B=map(int,input().split())
  S=input()
  ans=10**20
  for i in range(N):
    tmp=A*i
    for j in range(N//2):
      if S[j]!=S[-j-1]: tmp+=B
    ans=min(ans,tmp)
    S=S[1:]+S[0]
  print(ans)