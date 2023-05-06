# practice task #8: hotel rooms

You are working for a hotel and your task is to write a program that generates a random room assignment for guests. The program should randomly select an available room number and assign it to the guest.

One guest can book 1, 2 or 3 rooms simultaneously (considering big families booking for a vacation together). If they were to book multiple rooms at once, make sure that the program cannot assign the same room twice.

> Extra tip: you can use *random.randint()* from the **random** module to generate the number.

## instructions
Write a program that gets 3 integers as an input: the *smallest available room number*, the *largest available room number* and the *number rooms booked* by the guest.

Generate and print randomly selected room numbers to the standard output.

an example run:
```
Std. Input:	
smallest room number: 1
largest room number: 99
rooms needed: 2

Std. Output:
room 1: #47
room 2: #81
```