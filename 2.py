from h21 import sales

for item in sales:
    if item["price"] > 5000:
        print(item["product"])