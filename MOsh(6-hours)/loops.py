# answer number 1
prices = [10, 20, 30]
total = 0
for item in prices:
    total += item
print(f"the total amount is {total}")

# answer number 2
numbers = [5, 2, 5, 2, 2]
for i in numbers:
    print("*" * i)

# or we can do like this
for count in numbers:
    output = ''
    for result in range(count):
        output += "*"
    print(output)

# Solving to remove duplicates in a list
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
new = numbers.copy()
# To loop around index
index = 0
while index < len(new) - 1:
    new_index = index + 1
    while new_index < len(new):
        if new[index] == new[new_index]:
            new.remove(new[index])
        else:
            new_index += 1
    index += 1
print(new)
