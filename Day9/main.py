programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# print(programming_dictionary["Bug"])

# Adding a new item to a dictioanary
programming_dictionary["Loop"] = "The action of doing something over and over again"

# Edit an item in a dictioanary
programming_dictionary["Bug"] = "A moth in your computer"

# print(programming_dictionary)

# Loop through a dictioanary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])