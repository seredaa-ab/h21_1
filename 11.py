from h21 import sales

# 1. Від меншої до більшої
by_price_asc = sorted(sales, key=lambda x: x["price"])
print(by_price_asc)

# 2. Від більшої до меншої
by_price_desc = sorted(sales, key=lambda x: x["price"], reverse=True)
print(by_price_desc)