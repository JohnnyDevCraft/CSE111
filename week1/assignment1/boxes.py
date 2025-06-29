import math

totalItems = input("Enter the number of items:")
itemsPerBox = input("Enter the number of items per box:")

boxes = math.ciel(totalItems / itemsPerBox)

print(f"For {totalItems} items, packing {itemsPerBox} items in each box, you will need {boxes} boxes.")
