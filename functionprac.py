def asterisker(random_word, guesses):
    result = ""
    for letter in random_word:
        if letter in guesses:
            print(letter)
        else:
            print("*", end="")

    return result


random_word = "car"
guesses = []
asterisker(random_word, guesses)
