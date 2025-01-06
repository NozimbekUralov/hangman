import random, os

words = {
    "words": [
        {"name":"tomato", "description":"red, circle"},
        {"name":"potato", "description":"yellow, round"},
    ]
}

random_word = random.choice(words["words"])

context = list("_" * len(random_word["name"]))


while True:
    
    print("description of the vegetable: ", random_word["description"])

    print(" ".join(context), end="\n\n")

    guess = input("Guess a letter: ").lower()

    if guess not in random_word["name"]:
        os.system("clear")
        print("Wrong guess")
    else:
        if guess in random_word["name"]:
            guesses = [i for i in range(len(random_word["name"])) if random_word["name"][i] == guess]
            os.system("clear")
            for i in guesses:
                context[i] = guess

        if "_" not in context:
            os.system("clear")
            
            print("description of the vegetable: ", random_word["description"])

            print(" ".join(context), "You won!", sep="\n")
            
            break