# answer to find the largest number in a list
numbers = [3, 6, 2, 8, 4, 10]
largest_numbers = 0
for n in numbers:
    if largest_numbers < n:
        largest_numbers = n
print(f"the largest number is {largest_numbers} ")

# 2d list

matrix = [
    [1, 3, 3],
    [3, 21, 5],
    [6, 4, 1]
]
print(matrix[0:1])
"""This is the list slicing not indexing it starts from 0 row included then ends in 1 row
excluded So the first row is printed"""

print(matrix[0][0])
"""This is the first element of the first the first element"""

# Iterating the matrix but the list is printed vertically
for row in matrix:
    for col in row:
        print(col)

print("\n")

# List Methods
List = [5, 2, 1, 7, 4, 1]

# below function add a new integer in the List returns null so printing it shows null
print(List.append(1))

# prints the list in the terminal
print(List)

# below methods add integer in a given a index
List.insert(1, 20)
List.remove(20)
List.clear()
List.pop()
List.index(5)
print(0 in List)
print(List.count(1))
List.sort()
List.reverse()
print(List)
List2 = List.copy()

