def isPrime(number):
   num = int(number/2 )+1 
   for count in range (2, num):
       if(number % count == 0):
        return False
   return True
    

number = 14
print(isPrime(number))
