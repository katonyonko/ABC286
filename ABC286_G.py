import io
import sys

_INPUT = """\
6
6 6
1 3
2 3
3 4
4 5
4 6
5 6
4
1 2 4 5
6 5
1 2
1 3
1 4
1 5
1 6
3
1 2 3
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  def dfs(G,r=0):
      st=[]
      st.append(r)
      while st:
          x=st.pop()
          if used[x]==True:
              continue
          used[x]=True
          group[x]=r
          for v in G[x]:
              if v==parent[x]:
                  continue
              parent[v]=x
              st.append(v)

  N,M=map(int,input().split())
  G=[[] for _ in range(N)]
  G2=[[] for _ in range(N)]
  edge=[list(map(lambda x:int(x)-1,input().split())) for _ in range(M)]
  K=int(input())
  x=list(map(lambda x:int(x)-1,input().split()))
  t=set(x)
  y=list([i for i in range(M) if i not in t])
  for i in range(M-K):
    U,V=edge[y[i]]
    G[U].append(V)
    G[V].append(U)
  used=[False]*len(G)
  parent=[-1]*len(G)
  group=[-1]*len(G)
  for i in range(N):
    if used[i]==True: continue
    dfs(G,i)
  for i in range(K):
    U,V=edge[x[i]]
    u,v=group[U],group[V]
    G2[u].append(v)
    G2[v].append(u)
  ans=0
  for i in range(N):
    if len(G2[i])%2==1:
      ans+=1
  if ans<=2: print('Yes')
  else: print('No')