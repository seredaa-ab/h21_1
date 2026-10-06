from h21 import sales
max_item = sales[0]
for item in sales:
    if item["price"] > max_item["price"]:
        max_item = item

print(max_item["product"])
print(max_item["price"])