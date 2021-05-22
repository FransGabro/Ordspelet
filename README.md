# Ordspelet

**Version 1.0.0**

Ordspelet is a game where you and a program take turn on thinking on a word and guessing on wich word that was intended.

The game is divided in two parts. Part one where you guess on a word that the program is thinkig off and part 2 where you are going to think of a word from a list and the computer is going to guess on wich word you are thinking about. 
In both parts you will take turns on giving clues that is going to make it easier.

---
## Optional Setup

### Virtual environment 
[Venv](https://docs.python.org/3/library/venv.html)

* Linux/OSX
python -m venv .venv
source .venv/Scripts/activate

* Windows - cmd.exe
python -m venv .venv
.venv\Scripts\activate.bat

* Windows - PowerShell
> You  On Microsoft Windows, it may be required to enable the Activate.ps1 script by setting the execution policy for > > the user. You can do this by issuing the following PowerShell command:
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

py -m venv .venv
.\.venv\Scripts\Activate.ps1

---

## Contributors

- Frans Gabro <Frans.Gabro93@gmail.com>

---

## Rules

### Rules for part 1
It’s simple, the program is thinking of a word that has 5 letters and you are going to guess the right word. You will get two clues each time you are guessing. The clues are if your guessed word has any correct letters in the right word and if your supposed correct letter is in the right place of the word. When you finally guess the right word, you will get a "Rätt!" message.

### Rules for part 2
In part two it will be reversal of roles, you will think of a word from a list and the program is going to guess the word that you are thinking of. This time you will give clues to the program by writing two different numbers seperated with a comma. ex("1,2") The first number symbolizes how many correct letters the computer has in your word. The second number symbolizes how many correct letters that are in the right position of the word. Note, if a letter is in the right position you CAN’T count it on the first number only on the second.

Example: You are thinking of the word "polis" and the program is guessing on "solat". The word polis has 3 correct letters of which 2 is on the right place. You only type in 1 right letter in the word and 2 on the right letter on the right place. 
<1,2>

### Criteria
The criteria for the word that you and the program will use, is that it’s only allowed to contain exact 5 letters. The word may not have the same character two times in a row. E.g the word "alltid" is not allowed because of the 2 "l" that are after each other.
