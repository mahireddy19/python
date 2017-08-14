num1 = 10
num2 = 20
print("num1 + num2 =",num1+num2)
print("num1 - num2 =",num1-num2)
print("5^3",5**3);
print("20 % 3",20%3)
num3 = num1+num2
print(num3)
num3+=num2 #num3 = num3+num2
print(num3)
print("num 3 > num 2?",num3 > num2)
x=True
y=False
print("x and y",x and y)
print("x or y",x or y)
print("not of x",not x)

num4 = 7 #111
num5 = 6 #110
print('bitwise and =',num4 & num5)
print('bitwise or=',num4 | num5)
print('bitwise nor=',num4 ^ num5)

string1 = 'mahendra'
string2 = 'reddy'

print(string1+string2)
print(string1*3)
print(string2[1:3])
print(string1[:-1])
print(string1.count('a'))
print(string1.find('h'))
print(string1.split(','))
print(string1.upper())
print(max(string1))
print(min(string1))

tup = ('mahi','reddy','chintala','waste')
print(tup+('fellow','m'))

print(tup * 2)

print(tup[-1])

list1 = ['mahi','chinna','1989']
list1.append('19')
print(list1)

dict = {1:'mahi',2:'reddy'}
print(dict[1])
print(len(dict))


num = int(input('enter the value of n ='))
if(num<=0):
    print('enter a valid no')
else:
    sum=0
    while(num>0):
        sum+=num
        num-=1
    print(sum)
a = 2
b = 4
def add(a , b):
    res = a + b
    return res
num6 = 2
num7 = 4
print(add(num6 , num7 ))
'''
def fibo(n):
    a = 0
    b = 1
    for x in range(n):
        a=b
        b=a+b
        print(a,'\n')
    return b
num8 = int(input("enter value of n ="))
print(fibo(num8))
'''
file = open("/home/mahendra/mahi19",'r+')
print("file contents before writing")
print(file.read())
file.write("\n python is good")
print("file after writing")
file.seek(0)
print(file.read())

