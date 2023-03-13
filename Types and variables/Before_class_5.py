#Numbers

n1=3+5

n2=48-3*7

n3= (24-5*6)/3

n4=9/2

n5=17//4

n6=17%4

n7=7**8

width=34
height=6*3
n8=width*height

n9=3*1.25-2

tax=13.25/100
price=115.50
n10=price*tax
n11=price+n10
n11=round(n11,1)


#Strings

print('Hello World')

print('don\'t')

print("don't")

print('"Yes," they said.')

print("\"Yes,\" they said.")

print('"Isn\'t," they said.')

x='First line.\nSecond line.'
print(x)

print('C:\some\name')
print(r'C:\some\name')

print(2*'co'+'nut')
print('py''thon')

print('Put several strings within parentheses' 'to have them joined together.')

prefix='py'
sufix='thon'
print(prefix+sufix)

word='Hello World'
print(word[3], word[6])
print(word[-2], word[-6])

print(word[3:8])
print(word[6:])
print(word[-5:])

print(word[5:]+word[:-5])

s = "Pseudopseudohypoparathyroidisms"
print(len(s))


#Lists

numbers=[1, 2, 3, 4, 5 ,6]
print(numbers)

print(numbers[1])
print(numbers[-3])

print(numbers[3:])
print(numbers[-3:])
print(numbers+[10, 13, 15, 16])

print(len(numbers))


#First Steps

i = 379*379
print("The value of i is", i)

a, b = 0, 1
while a <1000:
    print(a, end=',')
    a, b = b, a+b