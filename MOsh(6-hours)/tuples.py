# Tuples
numbers = (2, 4, 7, 9, 2)
print(numbers.count(2))
print(numbers.index(9))
print(numbers)

# unpacking
x, y, z, a, b = numbers  # we have to unpack all the values

# Dictionary

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer.get("name"))
print(customer.get("birth_date", "15"))

# Question practice
phone = input("Phone: ")
dictionary = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

# or it can be solved
output = ""
for i in phone:
    ans = dictionary.get(i, "NOT FOUND NIGRU")
    output += ans + " "
print(output)

for i in phone:
    if i in dictionary:
        print(dictionary[i], end=" ")
        # The end keyword remove the "\n" which is added in the end in print function

# Reusable function emoji convertor
emoji_convertor_input = input("Say something with emojis: ")


def emoji_convertor(something):
    answer = ""
    dic = {
        ":)": "😁",
        ":(": "😠"
    }
    for emoji in something:
        answer += dic.get(emoji, emoji) + " "  # Everything will print in a same line in console
    return answer


print(emoji_convertor(emoji_convertor_input))
