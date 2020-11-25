# This program asks for a name and then prints greetings for them
import random

comma = ","
greetingsList = ["Hola","Konichiwa","Sat sri akall","Hello","Namaste"]

# Logic
name = input ("What is your name?")
greeting = random.choice(greetingsList)
print(greeting+comma, name)