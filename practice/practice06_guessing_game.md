# practice task #6: guessing game

You want to make a simple game. Here are the rules of this RNG-based game:

- computer “thinks” of a number between 1 and 20
- you have to guess the number
- you can score 100 points if you nail your guess
- otherwise, you lose 10 points per distance
- you can’t score less than 0 points

> Extra tip: you can use *random.randint()* from the **random** module to generate the number.

## examples
number: 1  
guess: 19  
score: 0

number: 20  
guess: 18  
score: 80

number: 17  
guess: 10  
score: 30

number: 5  
guess: 5  
score: 100

## instructions
Write a program that generates a random number, then gets an integer from the standard input.
Print the *number*, the *guess* and the *score* to the standard output.

an example run:
```
Std. Input:	
I thought of a number between 1 and 20. Your guess: 5

Std. Output:
number: 6
guess: 5
You scored 90 points!
```