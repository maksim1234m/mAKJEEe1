#1

s = input()
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])
print(len(s))
#2
print(input().count(' ') + 1)
#3
s = input()
print(s[(len(s) + 1) // 2:] + s[:(len(s) + 1) // 2])
#4
s = input()
first_word = s[:s.find(' ')]
second_word = s[s.find(' ') + 1:]
print(second_word + ' ' + first_word)
#5

s = input()
if s.count('f') == 1:
    print(s.find('f'))
elif s.count('f') >= 2:
    print(s.find('f'), s.rfind('f'))
    
    #6
    s = input()
if s.count('f') == 1:
    print(-1)
elif s.count('f') < 1:
    print(-2)
else:
    print(s.find('f', s.find('f') + 1))
    #7
    s = input()
s = s[:s.find('h')] + s[s.rfind('h') + 1:]
print(s)
#8
s = input()
a = s[:s.find('h')] 
b = s[s.find('h'):s.rfind('h') + 1]
c = s[s.rfind('h') + 1:]
s = a + b[::-1] + c
print(s)
#9
print(input().replace('1', 'one'))
#10
print(input().replace('@', ''))
#11
s = input()
a = s[:s.find('h') + 1] 
b = s[s.find('h') + 1:s.rfind('h')]
c = s[s.rfind('h'):]
s = a + b.replace('h', 'H') + c
print(s)
