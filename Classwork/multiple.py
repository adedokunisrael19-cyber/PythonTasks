"""take an input
find a range of 1 - 10
reiterate the process until it gets to 12
"""
number = int(input("enter a number"))
for num in range(1, 11):
   multiplication = num * number
   print(f"{number} X {num} =", multiplication)
