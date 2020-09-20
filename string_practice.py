hello = "Hello World!"

print(hello)

# Ask the user for their name

name = input("What is your name? : ")

print("It is so nice to meet you")

# Ask the user for their age

age = input("So.. tell me about yourself. How old are you? : ")

print("Wow, that old?")

# Ask the user what city they grew up in

city = input("You don't seem like you're from around here. Where did you grow up? : ")

# Ask the user what they enjoy

enjoy = input("I've never been there. What kinds of things do you like to do? : ")

# Create the output text

string = "Your name is {} and you are {} years old. You grew up in {}. Oh and by the way, you love {}."
output = string.format(name, age, city, enjoy)

# Print the output to the screen

print(output)
