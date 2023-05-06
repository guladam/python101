# practice task #9: lazy design ideas

You are working for a fashion company and your task is to write a program that generates a random outfit for a customer. The program should randomly select colors for items such as a top, bottom, and shoes and output the outfit to the user.

Colors can be generated using an RGB code. RGB stands for Red, Green, Blue and each value's intensity is described by a number between 0 and 255 where 0 means 0% and 255 means 100%.

But there's a twist: the user can provide a color preference for their clothes. If they pick *Red* for example, you need to make sure the program takes red with **at least 75%** intensity. However, providing a preference is optional.

> Extra tips: 
> 1: you can use *random.randint()* from the **random** module to generate the number.
> 2: what gets stored in a variable if you just press enter without typing anyting?

## instructions
Write a program that gets a string as an input: the color preference of the user: the value is either *"red"*, *"green"*, *"blue"*, or omitted.
Generate and print randomly selected colors to the standard output for their top, bottom and shoes.

an example run:
```
Std. Input:	
preference: red

Std. Output:
top: RGB(255, 0, 99)
bottom: RGB(237, 120, 246)
shoes: RGB(221, 35, 78)
```