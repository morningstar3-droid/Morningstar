
'''
Login info interface
'''
Name_1 = input('Enter your full name: ').title().strip()
username = input('Enter your username: ').capitalize().strip()

'''
set coditions for the login info, this function checks if the username & password are up to 18 character & have the pass word have symbols 
'''
#this part for the Name_1 conditional & workflow structure
symbols = "!@#$%&*_"

if len(Name_1) <= 3:
   print("use more character's")
elif len(Name_1) >= 10:
    print("Error not more than 10 character's")
elif any(ops in symbols for ops in Name_1):
    print("Sorry, No symbols are allowed in Full name: {Name_1}")
else:
    print("correct:)")


while any(c in symbols for c in Name_1) :
    print(f"NO symbols allowed in name: {Name_1}")
    Name_1 = input("Enter your full name: ").title().strip()


# this function checks for symbols in the Name input & if there's any form of symbol in it 
def check_for_symbols():
    symbols_1 = ["!@#$%^&*_-+"]
    if len(symbols_1) in Name_1:
        print("Sorry, but no symbols are allowed ")
        symbols_1 = check_for_symbols()
        Name_1 = input('Enter your username: ').capitalize().strip()
    else:
        print("Correct this time ")


#if any(char in symbols for char in Name_1 ):
#    print("Sorry, No sumbols area allowed in full name")

#Username Section
#this part is for the username conditional & workflow structure
    if len(username) <= 3:
        print("username is too short, use more character's")
    elif len(username) >= 18:
        print("Error not more than 18 character's")
    else:
        print(f"{username} is accurate. :)")

########################################################################
def check_for_symbols():
    symbols_1 = ["!@#$%^&*_-+"]
    if any (char in symbols_1 for char in username):
        print(f"""
NO Symbols: {symbols_1} are in Username: {username}, pleas add symbols
NO Symbols: {symbols_1} are in Username: {username}, pleas add symbols
              """)
        username = input('Enter your username again: ').capitalize().strip()
        symbols_1 = check_for_symbols()
    elif not any (ops in symbols_1 for ops in username):
        print(f"Atleast one or two symbols: {symbols_1} in the username " )
        username = input("Enter your username one more time: ").capitalize().strip()
    else:
        print(f"Username: {username} is correct")

        return check_for_symbols

def vaild_username():
    while len(username) != len(Name_1):
        print("Username can't the same name as full name try again.")
    input("Enter your username again")
    if  len(Name_1) == username:
        print("USERNAME: {username} CAN'T BE THE SAME AS FULL NAME {Name_1}")
    else:
        print("Username: {username} is vaild")

#########################################################################

#this part is for the password conditional & workflow structure
password = input('Create a Password: ').strip()
symbols = '!@#$%^&*_-+'

if len(password) <= 3:
    print("Password is too short, add more characteer's and symbols")
elif len(password) >= 19:
    print("Error not less than 19  character's and symbols")
elif not any(c in symbols for c in password):
    print("Password must include at least one symbol")
else:
    print("Password OK")

def vaid_password():
    while len(password) != username != Name_1:
        print(f"""
        Password: {password} can't have the same character's as Username: {username} & Full name: {Name_1}
""")


#the next idea for this scramble game is to add a timer for the user to guess the fruit within a certain amount of time, and if they don't guess it within that time, they lose the game.
#the next idea for this scramble game is to add a score system for the user to keep track of how many fruits they guessed correctly and how many they guessed incorrectly, and at the end of the game, they can see their score.
#the next idea for this scramble game is to add a leaderboard for the user to see how they rank against other players, and they can also see the top players and their scores.
#the next idea for this scramble game is to add a hint system for the user to get a hint if they are stuck on a fruit, and they can use the hint to help them guess the fruit correctly.
#the next idea for this scramble game is to add a multiplayer mode for the user to play against other players, and they can also see their friends' scores and compare them to their own.
#thhe next idea for this scramble game is to add a level system for the user to progress through different levels of difficulty, and as they progress, the fruits will become more difficult to guess.


#1. Add a timer for the user to guess the fruit within a certain amount of time, and if they don't guess it within that time, they lose the game.
#this is a list of fruits that will be used to generate a random fruit for the user to guess
#this list is a collection of fruits that will be used to generate a random fruit for the user to guess
fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli fruit", "vanilla bean", "watermelon", "xigua", "yellow passion fruit", "zucchini", "kiwi", "lemon", "lime", "blueberry", "blackberry", "cantaloupe", "honeydew", "kumquat", "mandarin", "olive", "persimmon", "pomegranate", "rhubarb", "starfruit", "tomato", "ugli fruit", "vanilla bean", "watermelon", "xigua", "yellow passion fruit", "zucchini", "kiwi", "lemon", "lime", "blueberry", "blackberry", "cantaloupe", "honeydew", "jackfruit", "kumquat", "lychee", "mandarin", "olive", "persimmon", "pomegranate", "rhubarb", "starfruit", "tomato", "ugli fruit", "vanilla bean", "watermelon", "xigua", "yellow passion fruit", "zucchini", "kiwi", "lemon", "lime", "blueberry", "blackberry", "cantaloupe", "honeydew", "jackfruit", "kumquat", "lychee", "mandarin", "olive", "persimmon", "pomegranate", "rhubarb", "starfruit", "tomato", "ugli fruit", "vanilla bean", "watermelon", "xigua", "yellow passion fruit", "zucchini", "kiwi", "lemon", "lime", "blueberry", "blackberry", "cantaloupe", "honeydew", "jackfruit", "kumquat", "lychee", "mandarin", "olive", "persimmon", "pomegranate", "rhubarb", "starfruit", "tomato", "ugli fruit", "vanilla bean", "watermelon", "xigua", "yellow passion fruit", "zucchini", "kiwi", "lemon", "lime", "blueberry", "blackberry", "cantaloupe", "honeydew", "jackfruit", "kumquat", "lychee", "mandarin", "olive", "persimmon", "pomegranate", "rhubarb", "starfruit", "tomato", "ugli fruit", "vanilla bean", "watermelon", "xigua", "yellow passion fruit", "zucchini", "kiwi", "lemon", "lime", "blueberry", "blackberry", "cantaloupe", "honeydew", "jackfruit", "kumquat", "lychee", "mandarin", "olive", "persimmon", "pomegranate", "rhubarb", "starfruit", "tomato", "ugli fruit", "vanilla bean", "watermelon", "xigua", "yellow passion fruit", "zucchini", "kiwi", "lemon", "lime", "blueberry", "blackberry", "cantaloupe", "honeydew", "jackfruit", "kumquat", "lychee", "mandarin", "olive", "persimmon", "pomegranate", "rhubarb", "starfruit", "tomato", "ugli fruit", "vanilla bean", "watermelon", "xigua", "yellow passion fruit", "zucchini", "kiwi", "lemon", "lime", "blueberry", "blackberry", "cantaloupe", "honeydew", "jackfruit", "kumquat", "lychee", "mandarin", "olive", "persimmon", "pomegranate", "rhubarb", "starfruit", "tomato"]



# this part is for the user to guess the fruit from the scrambled letters, and they can type 'skip' to skip to the next fruit
import random
import time

#def add_timer(seconds):
    #for seconds_left in range(seconds, 0, -1):
        #print(seconds_left)
        #time.sleep(1)
    #("Time's up!")

f_word = random.choice(fruits)
letters = list(f_word)
random.shuffle(letters)
scrambled = "".join(letters)
print(f"Scrambled word: {scrambled}")

#add_timer(30)



# this the fruits guessing structure if-elif-else statements it checks
#1. it take the fruits the username guessed 
#2. it comparre the spelling of the fruits the user had answered to with the orginal spelling of the fruit
#3. if the user types skip the game just skips
#4. if the user says anything like i don't know or a wrong answer the game will respond with an answer 

Guess = input("Guess the fruit (or type 'skip' to skip): ").lower().strip()
if Guess == f_word:
    message = f"Correct! The fruit was {f_word.upper()}"
    print(message.lower().upper())
elif Guess == "skip":
    message = f"Skipped! The fruit was {f_word.upper()}"
    print(message.lower().upper())
elif Guess != f_word:
    message = f"Wrong! The fruit was {f_word.upper()}"
    print(message.lower().upper())
else:
    print("Invalid input! Please try again.")


