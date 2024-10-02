#Start of Program
#----SterlingBot AI v2.0 @2024----
#------Python Coding Testing Grounds------

#Load Program
import time
import sys

def progress_bar(duration=5):
    for i in range(0, 101, 2):  # 2% increment
        sys.stdout.write("\r[" + "=" * (i // 2) + " " * (50 - i // 2) + "] " + str(i) + "%")
        sys.stdout.flush()
        time.sleep(duration / 50)  # Adjust speed here
    print()

progress_bar()

#--------------------------------

#Introduction & Animation Start
import time

# Function to animate text (typing effect)
def animate_text(text, delay=0.08):
    red_text = '\033[91m' + text + '\033[0m'  # Add red color ANSI code to the text
    for char in red_text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Move to the next line after the text is printed

# Example usage
animate_text("Hello, world!", 0.08)

#------------------------------------------

print()
time.sleep(2)
animate_text("What's your name?")
name_input = input("Type name here: ")

if name_input == "Chris":
    animate_text("I'm sorry, you must hate that name.")
else:   
    animate_text(f"Hi, {name_input}! Nice to meet you.")
animate_text("I am SterlingBot")

#---------------------------------------------

# Basic Math
print()
time.sleep(2)
animate_text("I can add numbers together.")

# Function to get a valid number input
def get_number_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            number = int(user_input)  # Convert input to an integer
            return number
        except ValueError:
            animate_text("Really? Come on, now. Please enter a valid number.")

# Get valid input for both numbers
number1 = get_number_input("Enter a number: ")
number2 = get_number_input("Enter another number: ")

# Calculate the result
animate_text(f"and that comes to: {number1 + number2}")

#---------------------------------------------

# Age Comparison
print()
time.sleep(2)
animate_text("How old are you?")
age_input = input()
age = int(age_input)
bot_age = 1

age_difference = age - bot_age
animate_text(f"You are {age_difference} years older than me. I'm only {bot_age} year old.")

#----------------------------------------------

# Ask the user for their favorite color
print()
time.sleep(2)
color_input = input("What's your favorite color? ")

# Convert the user's input to lowercase to handle case insensitivity
color_input = color_input.lower()

# Check the user's input and return different responses based on their answer
if color_input == "black":
    animate_text("Ah, a love for the dark I see. Nice.")
elif color_input == "pink":
    animate_text("Pink, huh? Very vibrant. You know, it doesn't have to be just a girly color.")
elif color_input == "green":
    animate_text("Green. A color symbolic of nature.")
else:
    animate_text(f"Oh, {color_input} is a cool color choice. Not one of my favorites but I have nothing against it.")
    
#‐-----------‐-‐--‐---------‐‐--‐------------

#---Choices---
print()
time.sleep(2)

def ask_to_continue():
    # Ask if the user wants to answer questions
    response = input("Would you like to answer some multiple-choice questions? (yes or no): ").strip().lower()

    if response == "yes":
        ask_question()  # Call the function to ask the questions
    elif response == "no":
        animate_text("Okay, skipping the questions!")
        next_task()  # Call the next function or task
    else:
        animate_text("Invalid input. Please type 'yes' or 'no'.")
        ask_to_continue()  # Recursively ask again for valid input

def ask_question():
    animate_text("What is the capital of France?")
    animate_text("A) Berlin")
    animate_text("B) Madrid")
    animate_text("C) Paris")
    animate_text("D) Rome")
    
    # Get the user's choice
    choice = input("Enter your choice (A, B, C, or D): ").strip().upper()

    # Check the answer
    if choice == "C":
        animate_text("Correct! Paris is the capital of France.")
    elif choice in ["A", "B", "D"]:
        animate_text("Incorrect. Try again!")
    else:
        animate_text("Invalid choice. Please choose A, B, C, or D.")
        ask_question()  # Recursively ask the question again for invalid input

def next_task():
    # Placeholder for the next task or function
    animate_text("Proceeding to the next part of the program...")

# Start by asking if they want to continue
ask_to_continue()

#------Choices--End--------------------‐------‐--
    
#Outro

time.sleep(6)
print()

animate_text("This is the end..........for now......")
    
#-----------End of Program-----------    
