#1 Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.

number = 1

while number <= 1000:

    if number % 3 == 0:

        print(number)


    number += 1

#2 Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.


while True:

    inches = float(input("Enter a length in inches "))


    if inches < 0:
        print("Program ended.")
        break


    centimeters = inches * 2.54


    print(f"{inches} inches is equal to {centimeters} centimeters")

# 3 Write a program that asks the user to enter numbers until they enter an empty string to quit. Finally, the program prints out the smallest and largest number from the numbers it received.

numbers = []
while True:
    user_input = input("Enter a number (or press Enter to quit): ")

    if user_input == "":
        break


    if user_input.replace(".", "", 1).isdigit() or (
            user_input[0] == "-" and user_input[1:].replace(".", "", 1).isdigit()):
        number = float(user_input)
        numbers.append(number)
    else:
        print("Invalid input. Please enter a valid number.")


if numbers:
    smallest = min(numbers)
    largest = max(numbers)

    # Print the smallest and largest numbers
    print(f"The smallest number entered is: {smallest}")
    print(f"The largest number entered is: {largest}")
else:
    print("No numbers were entered.")


#4Write a game where the computer draws a random integer between 1 and 10. The user tries to guess the number until they guess the right number. After each guess the program prints out a text: Too high, Too low or Correct. Notice that the computer must not change the number between guesses.



import random

target_number = random.randint(1, 10)

guesses = 0

while True:
    user_guess = int(input("Guess the number between 1 and 10: "))

    guesses += 1

    if user_guess == target_number:
        print(f"Correct! You guessed the number {target_number} in {guesses} guesses.")
        break
    elif user_guess < target_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")

#5 Write a program that asks the user for a username and password. If either or both are incorrect, the program ask the user to enter the username and password again. This continues until the login information is correct or wrong credentials have been entered five times. If the information is correct, the program prints out Welcome. After five failed attempts the program prints out Access denied. The correct username is python and password rules.

correct_username = "python"
correct_password = "rules"

attempts = 0

while attempts < 5:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == correct_username and password == correct_password:
        print("Welcome!")
        break
    else:
        print("Incorrect username or password. Please try again.")
        attempts += 1

if attempts >= 5:
    print("Access denied. You have reached the maximum number of login attempts.")


import random

def approximate_pi(num_points):
    inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)


        if x**2 + y**2 < 1:
            inside_circle += 1


    approx_pi = 4 * inside_circle / num_points
    return approx_pi


try:
    num_points = int(input("Enter the number of random points to generate: "))
    if num_points <= 0:
        print("Please enter a positive integer.")
    else:

        pi_approximation = approximate_pi(num_points)
        print(f"Approximation of pi using {num_points} random points: {pi_approximation}")
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")
