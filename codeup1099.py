# 코드업[1099]
a=[]
for i in range(10):
    b=list(map(int, input().split()))
    a.append(b)
i=1
j=1
while True:
  if a[i][j]==2:
    a[i][j] = 9
    break
  elif a[i+1][j] == 1 and a[i][j+1] ==1:
    a[i][j] =9
    break
  a[i][j] = 9
  if a[i][j+1] == 1:
    i+=1
  elif a[i+1][j] == 1:
    j+=1
  else:
    j+=1
for i in range(10):
  for j in range(10):
    print(a[i][j], end=' ')
  print()
