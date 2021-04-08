import budget


food = budget.Category("Food")
food.deposit(400, "New deposit")
food.withdraw(10.15, "Cloth")
food.withdraw(15.89, "shopping")
print(food.get_balance())
clothing = budget.Category("Clothing")
clothing.deposit(200, "New deposit")
food.transfer(80, clothing)
clothing.withdraw(25.55, "Top")
clothing.withdraw(100, "jeans")
print(clothing.get_balance())
entertainment = budget.Category("entertainment")
entertainment.deposit(300, "New deposit")
clothing.transfer(40, entertainment)
entertainment.withdraw(30, "movie")
entertainment.withdraw(20, "music")

print(food)
print(clothing)
print(entertainment)