from h21 import sales

for item in sales:
    revenue = item["price"] * item["quantity"]
    print(item["product"], "->", revenue, "грн")