import random 

words = ["python", "apple", "computer", "school", "hangman"]





word = random.choice(words)





guessed_word = ["_"] * len(word)





guessed_letters = []





wrong_attempts = 0

max_attempts = 6



print("Welcome to Hangman Game!")



while wrong_attempts < max_attempts and "_" in guessed_word:



    print("\nWord:", " ".join(guessed_word))

    print("Remaining Attempts:", max_attempts - wrong_attempts)



    guess = input("Enter a letter: ").lower()



    if guess in guessed_letters:

        print("You already guessed this letter.")

        continue



    guessed_letters.append(guess)



    if guess in word:

        print("Correct Guess!")



        for i in range(len(word)):

            if word[i] == guess:

                guessed_word[i] = guess

    else:

        print("Wrong Guess!")

        wrong_attempts += 1



if "_" not in guessed_word:

    print("\nCongratulations! You guessed the word:", word)

else:

    print("\nGame Over!")

    print("The correct word was:",word)
