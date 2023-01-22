import io
import sys

_INPUT = """\
6
4
naan
4
near
8
national
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  S=input()
  print(S.replace('na','nya'))