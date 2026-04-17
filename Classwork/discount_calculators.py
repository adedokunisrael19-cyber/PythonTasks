"""if purchase is greater than 1000 and less than 1000 
    give a discount of 5%
    add the price + discount
if purchase is less than 10,0000 and greater 50,000
    give a discount of 10%
     add the price + discount
    
if purchase is greater than 50,0000 
    give a discount of 20%
     add the price + discount"""
    





purchase = int(input("Enter the purchase amount"))
if (purchase >=1000 and purchase <=10,000):
   percentage_discount = (5/100) * purchase
   price= percentage_discount + purchase
    
elif (purchase >10000 and purchase <=50,000):
   percentage_discount = (10/100) * purchase
   price= percentage_discount + purchase

elif (purchase >50,000):
   percentage_discount = (20/100) * purchase
   price= percentage_discount + purchase
print ("the discount received is", percentage_discount)
print("the price is", price)
