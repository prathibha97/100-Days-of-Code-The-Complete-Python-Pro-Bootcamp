################### Scope ####################

enemies = 1

# Modifying global scope
def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1


increase_enemies()
print(f"enemies outside function: {enemies}")


# Local scope
def drink_portion():
    potion_strength = 2
    print(potion_strength)


drink_portion()
#print(potion_strength) #cannot access this because it is locally defined

# global constants
PI = 3.14159
URL = "http://www.google.com"