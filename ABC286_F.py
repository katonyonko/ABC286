import io
import sys

_INPUT = """\
6
3 3 4 1 6 7 8 9 10 11 12 13 5 15 16 17 18 14 20 21 22 23 24 25 19 27 28 29 30 31 32 33 34 35 36 26 38 39 40 41 42 43 44 45 46 47 48 49 37 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 50 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 67 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 86
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  #拡張ユークリッド ax+by=gcd(a,b)となるようなx,yを求める。同時にgcdも求める
  #aとbが互いに素な時、xはmod bにおいてのaの逆元
  def ExtGCD(a, b):
      if b:
          g, y, x = ExtGCD(b, a % b)
          y -= (a // b)*x
          return g, x, y
      return a, 1, 0

  #mが素数と限らない場合にmod.mに置けるaの逆元（aとmが互いに素であることが必要十分条件）を求める関数
  def Inv(a,m):
      return ExtGCD(a,m)[1]%m

  # 中国剰余定理。以下を満たすxを求める
  # x≡b1 (mod.m1)
  # x≡b2 (mod.m2)
  import math
  def Ch_Rem(b1,b2,m1,m2):
      g,p,q=ExtGCD(m1,m2)
      d=math.gcd(m1,m2)
      lcm=m1*m2//d
      return (b1+m1//d*(b2-b1)*p)%lcm

  a=[4,9,5,7,11,13,17,19,23]
  M=108
  A=[]
  tmp=0
  for i in range(len(a)):
    A+=list(range(tmp+1,tmp+a[i]))+[tmp]
    tmp+=a[i]
  print(M)
  print(*[A[i]+1 for i in range(len(A))])
  B=list(map(lambda x:int(x)-1,input().split()))
  b=[]
  tmp=0
  for i in range(len(a)):
    b.append(B[tmp]-tmp)
    tmp+=a[i]
  ans=Ch_Rem(b[0],b[1],a[0],a[1])
  tmp=36
  for i in range(len(a)-2):
    ans=Ch_Rem(ans,b[i+2],tmp,a[i+2])
    tmp*=a[i+2]
  print(ans)