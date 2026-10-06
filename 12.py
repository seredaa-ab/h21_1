from h21 import sales

by_quantity = sorted(sales, key=lambda x: x["quantity"], reverse=True)

for item in by_quantity:
    print(item["product"], item["quantity"])