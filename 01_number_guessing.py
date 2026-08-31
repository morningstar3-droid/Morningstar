'''
this is a number guessing game just as the file says read along to understand 
'''

'''
DON'T CHANGE, REWRITE OR ADD ANYTHING UNLESS YOU HAVE PERMISSION FROM THE CREATOR

'''
import random
from re import I
import time

from click import password_option

Pasword_num = list(range(1,101))
Number_bank = list(range(1, 51))
symbols = "!@#$%^&*_+"


def get_name():
    Name_1 = str(input("Enter your full name: ")).strip().title()
    return Name_1

#this function is for the fullname 

Name_1 = get_name()
if len(Name_1) <= 3:
    print("use more character's for your name.")
elif len(Name_1) > 20:
    print(f"Error not more than 20 character's for your name.")
elif any(char in symbols for char in Name_1):
     print("Sorry, No symbols are allowed in fullname")
else:
    print(f"Correct {Name_1 + " "}")


#this part is for the username conditional & workflow structure
#what it does is that it 
# 1. checks if the the username is less than 3 
username = input("Create a username: ").strip()
if len(username) <= 3:
    print("username is too short, use more character's")
elif len(username) >= 20:
        print("Error not more than 20 character's")
elif len(username) == Name_1:
     print(f"Sorry, Username: {username} should not be the same as Fullname: {Name_1}")

username_1 = input("Try again, Create a username: ").strip()
while username_1 == Name_1:
    print(f"Try again, you should not use the same name '{Name_1}' as your username.")
    username_1 = input("Try again, Create a username: ").strip()



print(f"Username: {username_1} is correct")



#PASSWORD SECTION
#this part is for the password conditional & workflow structure
def get_password():
     password_option = input("Enter a Password: ")
     return password_option

'''

this function (def get_password()): take the user password 
{there if-elif-else block checks if the is less than 3 character's or more than 30 charcter,
       there must be a symbol to be added &
             if the user means all the conditions it prints Password accepted}
'''


password_option = get_password()
if len(password_option) <= 3:
     print("Use more character;s for your password.")
elif len(password_option) >= 30:
     print("Not more 20 character's ")
elif not any(c in symbols for c in password_option):
     print("password must include at least one symbol")
elif not any(c in Pasword_num for c in password_option):
     print("password must include at least one or two number")
elif len(username and Name_1) == password_option or len(Name_1 and username) != password_option:
     print(f"Can't use the same Name: {Name_1} and username: {username} for password: {password_option}")
else:
     print("Password accepted")


# this part is for the timer & number if-eif-else statements
 
#random.shuffle(number)
#print(f"guessed number: {number}")
'''
def add_timer(seconds):
     for seconds_left in range(seconds, 0, -1):
         print(seconds_left)
         time.sleep(1)
#     print("Time's Up! fool")

add_timer(30)
'''


#this function controls the guessing game & how the number works along with the time 
#
def guessing_number():
    guessing_number = random.choice(Number_bank)
    return guessing_number

Guess_number = int(input("Guess the Number under 30 seconds (or type 'Skip' to Skip): "))
if guessing_number == ["Skip" or "skip" or "Skips" or "SKIPS" or "SKIP" or "skips"].strip().lower():
      print(f"The number is: {guessing_number}")
elif guessing_number != Guess_number:
     print(f"Sorry, The number was: {guessing_number}, You can try again")
elif Guess_number == str():
     print("Sorry, just type the number not the words")
elif Guess_number == guessing_number:
     print(f"Correct, You guessed the number: {guessing_number}")
elif time.sleep(1) > 0:
     print(f"Sorry, Time up! fool")
else:
     print("You sore loser")


         
      




