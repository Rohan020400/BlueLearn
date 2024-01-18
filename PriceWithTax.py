# Design a program that takes the prices of items a user bought 
# and calculates the total cost, including tax
PriceTotal= 0
prices=(input("Enter the prices:").split())
for i in prices:
    i=int(i)
    PriceTotal+=i
grandtotal= 1.08*PriceTotal
print(grandtotal)