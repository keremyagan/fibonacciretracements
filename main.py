# Define minimum and maximum price points
price_min = 34 #df.Close.min()
price_max = 49.5 #df.Close.max()

# Fibonacci Levels considering original trend as upward move
diff = price_max - price_min
level1 = price_max - 0.236 * diff
level2 = price_max - 0.382 * diff
level3=price_max - 0.5 * diff
level4 = price_max - 0.618 * diff
level5 = price_max - 0.786 * diff

print("Level", "Price")
print("0 ", price_max)
print("0.236", level1)
print("0.382", level2)
print("0.5",level3)
print("0.618", level4)
print("0.786", level5)
print("1 ", price_min)
