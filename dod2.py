from h21 import sales

max_revenue = 0
max_product = None

for item in sales:
    revenue = item["price"] * item["quantity"]

    if revenue > max_revenue:
        max_revenue = revenue
        max_product = item["product"]
print(max_product, max_revenue)