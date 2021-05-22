import random


#slumpar ord från listan
def random_line(RandomWord):
    lines = open('words.txt').read().splitlines()
    return random.choice(lines)


word = random_line('test.txt')


guess_count = 0

game_start = True
while game_start == True:
    guess = input('Gissa på ett ord: ')
    if len(word) != len(guess):
        print('Du måste gissa på ett ord med 5 bokstäver. Det får inte vara samma bokstav bredvid varandra.')
        break
    if len(guess)==len(word):
        guess_count += 1

    # kontrollerar ifall orden har samma bokstav och på rätt index.
    alphabet_count = 0
    index_count = 0
    if word != guess:
        for alphabet in word:
            for letter in guess:
                if alphabet == letter:
                    alphabet_count += 1
        for i in range(len(word)):
            if word[i] == guess[i]:
                index_count += 1

    print(f'Rätt bokstäver i ordet: {alphabet_count}')
    print(f'Antal bokstäver på rätt plats: {index_count}')

    if word == guess:
        print('Rätt!')
        print(f'Antal gissningar: {guess_count}')
        game_start = False
