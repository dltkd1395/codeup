# 코드업[1098]
a, b = input().split()
a, b = int(a), int(b)
c = int(input())
d=[]

g = [[0 for col in range(b)] for row in range(a)]

for i in range(c):
  e=list(map(int, input().split()))
  d.append(e)
  if d[i][1]==0:
    for k in range(d[i][0]):
      g[d[i][2]-1][d[i][3]-1+k]=1
  elif d[i][1]==1:
    for k in range(d[i][0]):
      g[d[i][2]-1+k][d[i][3]-1]=1

for i in range(a):
  for j in range(b):
    print(g[i][j], end=' ')
  print()

