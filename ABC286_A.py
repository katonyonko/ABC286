import io
import sys

_INPUT = """\
6
8 1 3 5 7
1 2 3 4 5 6 7 8
5 2 3 4 5
2 2 1 1 1
2 1 1 2 2
50 100
10 2 4 7 9
22 75 26 45 72 81 47 29 97 2
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,P,Q,R,S=map(int,input().split())
  A=list(map(int,input().split()))
  print(*(A[:P-1]+A[R-1:S]+A[Q:R-1]+A[P-1:Q]+A[S:]))