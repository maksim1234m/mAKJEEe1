#1 Задача *Максимум*
n, m = (int(_) for _ in input().split())
A = [[int(elem) for elem in input().split()] for _ in range(n)]
 
idxi, idxj = 0, 0
maxelem = A[0][0]
for i in range(n):
  for j in range(m):
    if A[i][j] > maxelem:
      maxelem = A[i][j]
      idxi = i
      idxj = j
     
print (idxi, idxj)
#2 Задача *Снежинка*
n = int(input())
a = [['.'] * n for i in range(n)]
for i in range(n):
    a[i][i] = '*'
    a[n // 2][i] = '*'
    a[i][n // 2] = '*'
    a[i][n - i - 1] = '*'
for row in a:
    print(' '.join(row))
#3 Задача  *Шахматная доска*
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 + y1 + x2 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')
#4 Задача *ДИАГОНАЛИ, ПАРАЛЛЕЛЬНЫЕ ГЛАВНОЙ*
n = int(input())
a = [[abs(i - j) for j in range(n)] for i in range(n)]
for row in a:
    print(' '.join([str(i) for i in row]))
#5 Задача *Побочная диагональ*
n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
    a[i][n - i - 1] = 1
for i in range(n):
    for j in range(n - i, n):
        a[i][j] = 2
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()
#6 Задача *Поменть столбцы*
def swap_columns(a, i, j):
    for k in range(len(a)):
        a[k][i], a[k][j] = a[k][j], a[k][i]
 
n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
i, j = [int(i) for i in input().split()]
swap_columns(a, i, j)
print('\n'.join([' '.join([str(i) for i in row]) for row in a]))
#7 Задача *Змейка*
n, m = map(int, input().split())
for j in range(n):
    print(' '.join([str(i + 1 + m * j) for i in range(m)][::pow(-1, j)]))