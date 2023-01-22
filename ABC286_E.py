import io
import sys

_INPUT = """\
6
5
30 50 70 20 60
NYYNN
NNYNN
NNNYY
YNNNN
YNNNN
3
1 3
3 1
4 5
2
100 100
NN
NN
1
1 2
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  def WF(cost):
    for k in range(len(cost)):
      for i in range(len(cost)):
        for j in range(len(cost)):
          if cost[i][k]!=10**20 and cost[k][j]!=10**20:
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
    return cost
  N=int(input())
  A=list(map(int,input().split()))
  S=[input() for _ in range(N)]
  Q=int(input())
  cost=[[10**20]*N for _ in range(N)]
  cost2=[[10**20]*N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      if S[i][j]=='Y':
        cost[i][j]=10**12-A[j]
        cost2[i][j]=1
  cost=WF(cost)
  cost2=WF(cost2)
  for i in range(Q):
    U,V=map(lambda x: int(x)-1,input().split())
    if cost2[U][V]==10**20: print('Impossible')
    else: print(cost2[U][V],cost2[U][V]*10**12-cost[U][V]+A[U])