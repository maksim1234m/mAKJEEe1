#2019 Maksim Sergejev/Egor Simagin
#1
x = 1000
while True:
    print(x)
    x +=3
    if x ==1018:
        break
#2
x = 1 
while True:
    print(x)
    x +=2 
    if x == 113:
        break
#3
x = 90 
while True:
    print(x)
    x -= 5
    if x == -5:
        break
#4
x = 2
while True:
     print(x)
     x *=2
     if x >= 2097152:
         break
#5
a = 2
while a < 9999:
    print(a)
    a = 2*a-1
#7
n = int(input("Введите число: "))
x = 1
sum = 1
for x in range(1,n+1):
    sum *= x
    x += 1
    print(sum)
#9
a = int(input())
i = int(a ** 0.5)
while i >= 1:
   if(a % i == 0 and i != 1):
       print("Число составное")
       break
   if(i == 1):
      print("Число простое")
i = i - 1
#8
x = int(input())
for i in range(1,x+1):
    if (x%i==0):
        print(i)
#12
n = int(input())
sum = 0
while(n != 0):
   sum = sum + (n % 10)
   n = n //10
print(sum)
#11
neChet = 3
chet = 2

i = 3

while i <=20:
    if(i%2 != 0):
        neChet= 2 * neChet - 2
        print(neChet)
else:
    chet = 2 * chet -2
    print(chet)
i = i + 1
