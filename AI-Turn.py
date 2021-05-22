import random


class Words:  

    def __init__(self):
        self.list = []

    def load(self, path):
        self.list = open('words.txt').read().splitlines()   

    def rndm(self):
        return random.choice(self.list)

    def filter(self, guess, clue):
        self.filter_chr(guess, clue[0] + clue[1])
        self.filter_pos(guess,clue[1])
        return self.filter_guess(guess, clue)
        
    def filter_guess(self, guess, clue):
        '''
        Remove incorrect guess or return right answer
        '''
        if len(self.list)== 1:
            return guess
        else:
            self.list.remove(guess)  #wrong guess
            return None 

    def filter_chr(self, guess, n): 
        '''
        Tar bort alla ord som inte har minst lika många rätta bokstäver som "guess".
        Ett ord är dåligt om det har färre rätta bokstäver än "guess"  
        guess - senaste gissningen
        n - antal rätta bokstäver i guess
        '''
        for word in self.list:
            n2 = 0  # antalet bokstäver i ordet
            guess2 = list(guess)
            word2 = list(word)

            for i in range(len(guess)):
                for j in range(len(word)):
                    if word2[j] == guess2[i]:
                        word2[j] = '?'
                        n2 += 1
                        break

            if n > n2:
                self.list.remove(word)
                print(f'del:', word)
        
    def filter_pos(self, guess, n):
        '''
        Tar bort alla ord som inte har "n" bokstäver på samma plats som "guess"
        Ett ord är dåligt om det har färre rätta bokstäver på rätt plats än "guess"  
        guess - senaste gissningen
        n - antal rätta bokstäver på rätt position i guess
        '''
        for word in self.list.copy():
            n2 = 0  # antalet bokstäver i rätt position
            guess2 = list(guess)
            word2 = list(word)

            for i in range(len(guess)):        
                    if word2[i] == guess2[i]:
                        n2 += 1
            if n > n2:
                self.list.remove(word)
                print(f'del:', word)    

words = Words()
words.load('words.txt')
guess = words.rndm()
answer = None
while answer is None:
    guess = words.rndm()
    print(guess)
    clue = input(f'Rätta bokstäver,Rätta positioner: ').split(',')
    clue = [int(x) for x in clue]
    answer = words.filter(guess, clue)
    print(words.list)

print('Rätt ord!')
        

