import random

list_of_words = ["cannon", "pirate", "ship", "sword", "culverine", "frigate", "fluyt", "bucaneer", "island", "treasure", "musket", "rapier", "navaja", "cutlass", "spyglass", "parrot", "galleon", "schooner"]
word = random.choice(list_of_words)
word = list(word)
#______________________________________________GENERATE RANDOM WORDS
blanks = ""
for blank in word:
    blank = "_"
    blanks = blank + blanks
blanks = list(blanks)
#___________________________________BLANKS - Generates a corresponding list with "_" for each item in the list word
end_game = False
lives = 6
#___________________________________________CONDITIONS (endgame and lives)
gallows = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
#____________________________________________GRAPHICS LIST
while not end_game:
            
    letter = input("Choose a letter?")
    
    def generate_index():  #Generates indexes to match positions in list WORD with list BLANKS
        indices = []
        for i in range(len(word)):
            if word[i]==letter:
                indices.append(i)
        return indices
    
    index = generate_index()
    
    def write_letter():    #writes the corresponding letter from WORD in BLANKS
        for letter_index in index:
            blanks[letter_index]=l
        return(letter_index)
    
    for l in word:
        if l == letter:
            generate_index()
            write_letter()
            
    if letter not in word:
        lives = lives - 1
        if lives == 6:
            print(gallows[0])
        elif lives == 5:
            print(gallows[1])
        elif lives == 4:
            print(gallows[2])
        elif lives == 3:
            print(gallows[3])
        elif lives == 2:
            print(gallows[4])
        elif lives == 1:
            print(gallows[5])
        elif lives == 0:
            print(gallows[6])

    print(lives)
    print(blanks)

    if "_" not in blanks:
        end_game = True
        print ("YOU WON!")
    elif lives == 0:
        end_game = True
        print(f"The word you were looking for is {word} \nYOU ARE HANGED!")
