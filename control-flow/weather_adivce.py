Weather = input("What's is the weather like today? (sunny/rainy/cold): ")
# Weather recommendation
if Weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif Weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif Weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")