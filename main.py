import random, os

words = {
    "cities": ["London", "Washington DC", "Warsaw", "Paris"],
    "vegetables": [
        {"name":"tomato", "description":"red, circle"},
        {"name":"potato", "description":"yellow, round"},
    ]
}

random_word = random.choice(words["vegetables"])

context = list("_" * len(random_word["name"]))


while True:
    os.system("clear")
    
    print("description of the vegetable: ", random_word["description"])

    print(" ".join(context), end="\n\n")

    guess = input("Guess a letter: ").lower()

    if guess in random_word["name"]:
        guesses = [i for i in range(len(random_word["name"])) if random_word["name"][i] == guess]

        for i in guesses:
            context[i] = guess

    if "_" not in context:
        os.system("clear")
        
        print("description of the vegetable: ", random_word["description"])

        print(" ".join(context), "You won!", sep="\n")
        
        break