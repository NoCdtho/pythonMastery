"""Scope refers to where a variable or function name is available to be used. For example, when we create variables
in a function (such as by giving names to our parameters), that data is not available outside of that function."""


def get_max_health(modifier, level):
    return modifier * level


my_modifier = 5
my_level = 10

# don't touch above this line

max_health = get_max_health(my_modifier, my_level)

# don't touch below this line

print(f"max_health is: {max_health}")

"""Global Scope So far we've been working in the global scope. That means that when we define a variable or a 
function, that name is accessible in every other place in our program, even within other functions."""

# ?

# Don't touch below this line


player_level = 4


def calculate_health(modifier):
    return player_level * modifier


def calculate_primary_stats(armor_bonus, modifier):
    return armor_bonus + modifier + player_level


print(f"Character has {calculate_health(10)} max health.")

print(f"Character has {calculate_primary_stats(3, 8)} primary stats.")

