import math

def pizza_area(num_of_pizzas, diameter):
    return num_of_pizzas * diameter / 2 * diameter / 2 * math.pi

num_of_pizzas1 = int(input("number of bigger pizza(s) = "))
d_pizza_1 = int(input("diameter of bigger pizza(s) (in cm) = "))
num_of_pizzas2 = int(input("number of smaller pizza(s) = "))
d_pizza_2 = int(input("diameter of smaller pizza(s) (in cm) = "))

print("total area of bigger pizza(s):", round(pizza_area(num_of_pizzas1, d_pizza_1), 2))
print("total area of smaller pizza(s):", round(pizza_area(num_of_pizzas2, d_pizza_2), 2))