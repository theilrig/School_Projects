def mainOutput(price, size):
    pricePerSqIn = price/size
    print(f"The price per square inch of the pizza is {pricePerSqIn}")
    noOfSlices = 8
    chargePerSlice = price/noOfSlices
    print(f"One slice costs {chargePerSlice}")
    amountOnePersonEats = 5
    personsPerPizza = size/amountOnePersonEats
    print(f"One pizza can feed {personsPerPizza} people")

def mainPrompt():
    try:
        pizzaPrice = int(input("What is the price of your pizza: "))
    except ValueError:
        print("Please input an integer")
        mainPrompt()
    try:
        pizzaSize = int(input("What is the size of your pizza in square inches: "))
    except ValueError:
        print("Please input an integer")
        mainPrompt()
    mainOutput(pizzaPrice,pizzaSize)

mainPrompt()

    