principal= input("whats your principal amount:") 
rate= input("whats the rate:")
time= input("whats the time: :")
principal = int(principal)
rate=int(rate)
time= int(time)
simpleinterest = (principal * rate * time) / 100
amount = principal + simpleinterest
print ("the simple interest is", simpleinterest, "and the amount is ", amount)
