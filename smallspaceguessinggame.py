
secret_word = "Venus"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
         guess = input("Enter what is the hottest planet in our solar system: ")
         guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You loose!")
else:
    print("You won!")


secret_word = "Jupiter"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
         guess = input("Enter what is the biggest planet in our solar system: ")
         guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You loose!")
else:
    print("You won!")


secret_word = "82"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
         guess = input("Enter how many moons does saturn have: ")
         guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You loose!")
else:
    print("You won!")


secret_word = "Star"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
         guess = input("Enter sun is what: ")
         guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You loose!")
else:
    print("You won!")


