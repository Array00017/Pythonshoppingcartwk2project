foods = []
prices = []
total = 0 

while True:

    food = input("Enter a food to buy (quit): ")
    if food == "quit":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)
        
        
        
print("----- YOUR CART -----")    
    
for food in foods:
        print(food)
for price in prices:
    total += price 

print()
print(f"Your total is: ${total}")