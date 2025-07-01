import math

totalItems = input("Enter the number of items:")
itemsPerBox = input("Enter the number of items per box:")

boxes = math.ceil(float(totalItems) / float(itemsPerBox))

print(f"For {totalItems} items, packing {itemsPerBox} items in each box, you will need {boxes} boxes.")
