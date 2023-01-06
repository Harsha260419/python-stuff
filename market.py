stock = 100

while True:
    demand = int(input("Enter the demand: "))
    if demand <= stock and demand >= 0:
        print("Order placed")
        stock -= demand
        print(f"Available stock is {stock}")
    else:
        print(f"Not available, because the available stock is {stock}")
    for i in range(5):
        if stock == 0:
            print("sorry out of stock")
        elif stock <= 5:
            print(f"Hurry up only {stock} stocks left!!!")
        break
        break
