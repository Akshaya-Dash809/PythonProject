### Arithmatic Operator

print(5%2)   # 1
print(5/2)   # 2.5
print(5//2)  # 2 , this is float division
print(5**2)  # 25
print(5 + 2 * 3 -1 + 10 / 5 )  # 12.0
# calculate BMI
weight = 50
height = 1.8
print(weight/(height*height)) # 15.4

### Assignment Operator
print("_____________Assignment Operator_____________")
a = 5
a += 2 # 7 , a= a+2
a -= 2 # 5 , a= a-2
a *= 2
a /= 2
a //= 2
print(a)
a,b,c = 2,3,4
print(a,b,c) # 2 3 4

### Comparison / Relational Operator
print("__________comparison operator__________")
a=5
print(a>3) # True
print(a<3) # False
print(a>=3) # True
print(a<=3) # False
print(a==3) # False
print(a!=3) # True


### Logical Operator
print("_______Logical Operator______")
e,f = 5,4
print(e>f and e<f) # False
print(a>b or a<b)  # True

print(a>4 or b<10)  # True
print(a<4 or b<13)  # True

print(not(a>10)) # True
print((a<b) or not(a>b) ) # False
d=False
print(not (d)) # True

### Bitwise Operator
print("__________________Bitwise Operator___________")
x,y = 5,4
print(x & y)   # 4
print(x | y)   # 5
print(x^y)     # 1
print(~x)      # -6
print(~y)      # -5
print(x << 2)  # 20
print(x >> 2)  # 1
print(26 & 23) # 18
print(17 ^ 24) # 9
print(17 / 24) # 0.70833
print(~45)     # -46
print(68 << 2) # 272
print(56 >> 3) # 7

### Identity Operator  (is , is not)
print("____________Identity Operator____________")
m =5
n =5
print(m is n) # True
print(m is not n) # False
print(m == n) # True
print(id(m))
print(id(n))

j =5
k =5.0
print(j is k) # False
print(j is not k) # True
print(j == k) # True
print(id(j))
print(id(k))

c= 5
print(id(c))
c=7
print(id(c))
print(c is c) # True
print(c == c) # True

### Membership Operator (in , not in)
print("________________Membership Operator____________")
st = 'Akshaya'
print('k' in st) #True
print('k' not in st) # False
print('K' in st) # False
print('ksh' in st) # True
lst = [2,1,6,4,8,4,2]
print(8 in lst) # True
print(2 not in lst) #False

