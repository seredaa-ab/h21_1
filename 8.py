from h21 import sales
counter = 0

for item in sales:
    if item["category"] == "Electronics":
        counter += 1

print(counter)