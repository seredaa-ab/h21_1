from h21 import sales

for item in sales:
    if item["category"] == "Electronics" and item["price"] > 2000:
        print(item["product"], item["price"])
