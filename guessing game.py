secret_word="juniper"
guess=""
guess_count=0
guess_limit=3
out_of_guesses=False

print("What is your favorite vendor ?")

while guess != secret_word and  not(out_of_guesses):
    if guess_count < guess_limit:
        guess=input("Enter guess: ")
        guess_count=guess_count+1
    else: out_of_guesses = True
if  out_of_guesses:
    print("Out if guesses, YOU LOSE!")
else:
    print("You win !")