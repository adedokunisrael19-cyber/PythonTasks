principal = input("Type in the Principal")
rate=input("type in the interest")
duration=input("what is the duration")

principal= int(principal)
rate= int(rate)
duration = int(duration)
print(type(principal))
print(type(rate))
print(type(duration))
a= (1+rate)
b=(a**duration)-1
#c= b-1
d=a-1
e=(b/d)
print (e)
