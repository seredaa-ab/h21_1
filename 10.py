from h21 import sales

names = []

for item in sales:
    names.append(item["product"])

print(names)