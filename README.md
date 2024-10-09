# Pattern generator 
I recreated a [10 Print](https://10print.org) generator based on Emily Dennet’s  modifications of the pattern in *[Randomizing Your Digits: Generatively Knit Mittens](https://archive.bridgesmathart.org/2022/bridges2022-281.html)* from Bridges 2022. 

The generator has the option to take more than two choices for a base block, but is currently hard coded to take in the [[leftleaning.txt]] and [[rightleaning.txt]] blocks.

The program makes a random choice of pattern block from a
list, and appends them, and outputs the design. The user can decide the size of the grid that blocks are put into (currently hard coded to run several times in a row more easily), and (with a little bit of effort) which pattern blocks to read. 
The generator outputs the pattern in the terminal, and the user has the option to save it as a .txt file.

How to run: 
`python3 generate.py`


