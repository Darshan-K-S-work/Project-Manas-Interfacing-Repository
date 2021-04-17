from random import randint

try:
    from playsound import playsound
except:
    pass

totScore = [0, 0]


# Hangman graphics
hpics = ["""
    +---+   ____________________
    O   |   | Please don't let |
   /|\  |   | me die!          |
   / \  |   | _________________|
  =======   |/
  ~~~~~~~
  ~~~~~~~
""", """
   +---+   _______________________
   O   |   | My feet feel tingly.|
  /|\  |   | You can stop this!  |
  / \  |   | ____________________|
    ====   |/
 ~~~~~~~
 ~~~~~~~
""", """
   +---+   ____________________________
   O   |   | Ahh, I just lost a foot, |
  /|\  |   | stop this horror.        |
    \  |   | _________________________|
    ====   |/
 ~~~~~~~
 ~~~~~~~
""", """
   +---+   _____________________________
   O   |   | Maybe I can do fine being |
  /|\  |   | a cripple, but stop this! |
    \  |   | __________________________|
      ==   |/
 ~~~~~~~
 ~~~~~~~
""", """
   +---+   _____________________________
   O   |   | I just saw my bottom half |
  /|\  |   | fall down, help me!       |
       |   | __________________________|
      ==   |/
 ~~~~~~~
 ~~~~~~~
""", """
   +---+   ________________________________
   O   |   | I have no more limbs left!   |
   |   |   | I could live with some help. |
       |   | _____________________________|
      ==   |/
 ~~~~~~~
 ~~~~~~~
""", """
   +---+   _________________________________
   O   |   | Maybe I can still be a cyborg.|
       |   | Just catch what's left of me! |
       |   | ______________________________|
      ==   |/
 ~~~~~~~
 ~~~~~~~
""", """
   +---+   ____________
       |   | ...      |
       |   | Splosh!  |
       |   | _________|
      ==   |/
 ~~~~~~~
 ~~~~~~~
"""
         ]

# Words list
misc = {
    "android": "Famous Operating System",
    "bag": "Used to carry",
    "blood": "Red liquid",
    "building": "Humans live and work here",
    "clock": "Have this on phones now",
    "demon": "Scare you, but some worship them",
    "electricity": "Enabled modern technology",
    "family": "Feels like home anywhere with them",
    "fiction": "Limited by one\'s imagination",
    "garden": "Needs to be watered unless it rains",
    "gun": "Most used modern day weaponry",
    "hammer": "Used to nail it in",
    "hunter": "A cool job in medieval ages, sometimes not a lifestyle choice",
    "hangman": "Whatcha playin",
    "iron": "____ man is the best MCU character",
    "impulse": "A tiny wave or emotion",
    "island": "Surrounded by water",
    "jump": "Cats always land on their feet after doing this",
    "kettle": "Important appliance in the Hostel",
    "knife": "Stab the back",
    "library": "Go here to do a lot more than study",
    "lost": "That feeling since the pandemic started",
    "love": "That emotion portrayed well only in the movies",
    "military": "Armed forces",
    "needle": "Is being an actual prick",
    "night": "Best part of a day",
    "politics": "Probably shouldn\'t get into this",
    "protest": "Ends up mostly in a screaming group",
    "queen": "England\'s royalty who never dies",
    "rain": "Some dance when this occurs, some look for umbrellas",
    "rhythm": "Racist to say only Black people have it",
    "school": "Where we spend most of our childhood",
    "sunset": "Sun is going up/down",
    "town": "A smaller version of a city",
    "tomorrow": "The day after the night",
    "umbrella": "Need this to move in the rain",
    "unity": "Present in spite of diversity",
    "valorant": "A new one from Riot games",
    "work": "What you wish to be paid for after education",
    "xenon": "A noble gas that\'s cool to say",
    "yatch": "What you wish to buy living in a beach-house",
    "yellow": "A ripe colour",
    "zeus": "A prominent Norse god",
    "zoom": "A competitor to Microsoft Teams"
}
animals = {
    "animal": "Big general organisms",
    "bat": "Don\'t mess with me and cause a pandemic",
    "cat": "Best pets",
    "dog": "Second best pet",
    "gorilla": "Our ancestors",
    "python": "The language used for this game",
    "monkey": "The smaller descendents of primates",
    "elephant": "You can sit on it for a good ride",
    "sloth": "Moves way too slow",
    "lion": "The Lannister symbol",
    "wolf": "The Northern canines",
    "velocioraptor": "Group hunting dinosaurs",
    "crocodile": "Amphibian reptile from jurassic period"
}
entertainment = {
    "witcher": "A great series of games and recently a TV show",
    "vikings": "Great Norsemen, not too noble",
    "naruto": "A great anime",
    "bleach": "Cleaning agent, also an anime",
    "avatar": "Blue aliens",
    "mandalorian": "Renewed the star wars franchise after the sequel trilogy",
    "chernobyl": "Nuclear disaster",
    "dark": "Due to absence of EMW",
    "office": "A good sitcom and hope we have similar jobs",
    "friends": "We were on a break!",
    "interstellar": "Movie with wormholes & blackholes",
    "joker": "Batman\'s best villain",
    "godfather": "Al Pacino and criminal empire"
}
food = {
    "apple": "Fruit relates to doctors",
    "cheese": "Best part of pizza",
    "egg": "Always a part of a sunnyside breakfast",
    "jelly": "Wobbly food",
    "orange": "Color and fruit",
    "pizza": "Most consumed Italian dish",
    "spaghetti": "Great with meatballs and Italian",
    "bread": "Most consumed bakery product",
    "ramen": "Best japanese noodles variant",
    "coffee": "Beverage to keep you up",
    "tea": "Chamomile",
    "sushi": "Raw fish with rice",
    "unagi": "salmon skin roll",
    "biriyani": "Not pulao",
    "burger": "Buns and patty",
    "fries": "Almost rectangular potato pieces",
    "cookie": "____ and milk",
    "tacos": "When you hear Mexican",
    "samosa": "Almost triangular snacks",
    "manchurian": "Gobi",
    "dosa": "Famous flat South-Indian dish"
}


def intro_scr():  # Intro screen at game start
    try:
        import pyfiglet
        print("\n")
        title = pyfiglet.figlet_format(" "*25+"HANGMAN")
        print(title)
    except:
        print("\n"+"\t"*5+"H A N G M A N\n")
    print("\t"*8, "-Darshan K S\n")
    try:
        playsound('./Sounds/drums.wav')
    except:
        pass
    print("Press Enter".center(22, "\t"))
    input()


def desc():  # How to play and rules
    intro = """\n
    \tWelcome to Hangman. This is a word guessing game. 
    \tPretext:
    \t\tFollowing a criminal sentence, your friend is standing on a platform with a rope around his neck.
    \t\tBelow the platform is toxic waste sludge with fumes emanating from it.
    \t\tThe platform protects your friend from melting due to the vapours.
    \t\tFor every wrong guess, the platform breaks and he start melting for every wrong guess.
    """
    print(intro.center(15, '\t'), hpics[0])
    try:
        playsound('./Sounds/desc.wav')
    except:
        pass

    rules = """\n
    \tHOW TO PLAY:
    \t\t1. Start guessing letters by typing them in. The correct and wrong letters will be shown.
    \t\t2. You will have 6 lives while guessing the letters.
    \t\t3. After 3 lives are lost you will be given an option to get a hint.
    \t\t4. If you choose to take the hint you will have no more lives left to lose :)
    """
    print(rules.center(15, "\t"))


def lost_scr():  # Losing screen
    try:
        import pyfiglet
        print("\n")
        title = pyfiglet.figlet_format(" "*25+"YOU LOST")
        print(title)
    except:
        print("\n"+"\t"*5+"Y O U\tL O S T\n")
    try:
        playsound('./Sounds/lost.wav')
    except:
        pass


def win_scr():  # Winning screen
    try:
        import pyfiglet
        print("\n")
        title = pyfiglet.figlet_format(" "*25+"YOU WON")
        print(title)
    except:
        print("\n"+"\t"*5+"Y O U\tW O N\n")
    try:
        playsound('./Sounds/win.wav')
    except:
        pass


def play_again():  # Play again input
    print("Do you want to play again? (yes or no)")
    x = (input().lower().startswith('yes')) or (
        input().lower().startswith('Yes')) or (input().lower().startswith('YES'))
    return x


def get_word(words):  # Returns the secret random word
    i = randint(0, len(words)-1)
    return words[i]


# Display hangman, modified blanks and missed letters
def runtime_disp(missedLetters, correctLetters, guessWord):
    print(hpics[len(missedLetters)], "\n")

    blanks = "_" * len(guessWord)
    # Replacing blanks
    for i in range(len(guessWord)):
        if guessWord[i] in correctLetters:
            blanks = blanks[:i] + guessWord[i] + blanks[i+1:]

    # Display replaced blanks list
    for i in blanks:
        print(i, end=" ")
    print("\n")

    # Display missed letters
    print("Missed letters: ", end=" ")
    for l in missedLetters:
        print(l, end=" ")
    print("\n")


# Returns the letter entered and makes sure that only one letter is entered
def guess_input(alreadyGuessed):
    while True:
        print("Guess a letter.")
        guess = input("> ")
        guess = guess.lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in alreadyGuessed:
            print("You have already guessed this letter. Choose again.")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a LETTER.")
        else:
            return guess


def get_high():
    f = open("./Files/high_score.txt", "r")
    hi = int(f.read())
    return hi


def high():  # High Score
    hi = get_high()
    if (totScore[0] > hi):
        hi = totScore[0]
        # New Record screen
        try:
            import pyfiglet
            print("\n")
            title = pyfiglet.figlet_format(" "*15 + "New High Score")
            print(title)
        except:
            print("\t"*4+"New High Score\n")

        f = open("./Files/high_score.txt", "w")
        f.write(str(hi))
        f.close()
