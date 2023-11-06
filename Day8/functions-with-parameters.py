# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
  print("Hello")
  print("How do you do?")
  print("Isn't the weather nice today?")
  
# greet()

# Functions that allows for input

def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you do {name}")

# greet_with_name("Prathibha")

# Functions with more than one input

def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}")
  
# Positional arguments
# greet_with("Prathibha", "Kandy")

# Keyword arguments
greet_with(name="Prathibha", location="Kandy")