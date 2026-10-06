from h21 import sales
total = 0
for item in sales:
    total += item["quantity"]
print(total)