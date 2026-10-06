from h21 import sales
total_price = 0
for item in sales:
    total_price += item["price"]

average = total_price / len(sales)
print(average)