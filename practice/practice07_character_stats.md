# practice task #7: character stats

You are working for a video game company and the company is working on a new role-playing game (RPG).
In RPGs, the character strengths and weaknesses are usually described by different attributes.

In this game, players can spend their time to carefully distribute attribute points manually but for convenience the can just press a button to randomly generate attribute values.

Your task is to write the program that generates a random character for a new game. The program should randomly select attributes such as strength, agility, charisma, wisdom and intelligence and output the character to the user.

The attribute values should be between 1 and 15.

> Extra tip: you can use *random.randint()* from the **random** module to generate the number.

## instructions
Write a program for the character generator. Get the name of the character from the input as a string value.
Print the generated attributes to the standard output.

an example run:
```
Std. Input:	
name: Béla the Wise Monk

Std. Output:
Attributes of Béla the Wise Monk
------------------
strength: 5
agility: 3
charisma: 8
wisdom: 14
intelligence: 11
------------------
```