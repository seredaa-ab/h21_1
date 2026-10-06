from h21 import sales

min_item = sales[0]

for item in sales:
    if item["price"] < min_item["price"]:
        min_item = item

print(min_item["product"])
print(min_item["price"])