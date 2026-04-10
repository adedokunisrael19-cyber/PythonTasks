num = input("type s 5 digits number")
num=int(num)
num1=num//10000
num2=(num//1000)%10
num3=(num//100)%10
num4= (num%100)//10
num5 = num%10
print(num1,"\t",num2,"\t",num3,"\t",num4,"\t", num5)
