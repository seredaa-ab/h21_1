from h21 import sales

categories = set()              # empty set

for item in sales:
    categories.add(item["category"])

print(categories)