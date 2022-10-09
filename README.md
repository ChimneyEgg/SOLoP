# SOLoP

## Introduction
**SOLoP** ( Stack-Orientated Language of Programming ) is a simplistic stack-based programming language written in Python. It uses symbols to denote simple commands, and has a mostly easy learning curve. For procedures and commands, reverse-polish notation ( also called postfix notation ) is used, making it easier to perceive how the stack will be affected by a given command. 
SOLoP is more of an experiment than an actual product, made and designed in about a week. I guess it could be used for golf-scripting or just be considered an esoteric programming language ( though I would not consider it to be one.)
## Quickstart
Getting started with SOLoP is relatively easy, everything you need is already in the repository
### Building With Compile.exe
Using compile.exe we can easily interpret the .solo file. First download compile.exe to a folder, then do the following:
```
> cd [folder-name]

> .\compile.exe [filename]
```
### Building With Python
If you wish to build the SOLoP interpreter yourself, you first need a couple of things:
- A Python compiler ( see: https://www.python.org/downloads/ )
- Command Line / IDE

Once you have acquired those requirements, you can take the compile.py file and run it in a command line interface:
```
> python compile.py [filename]
```
### Making a file
Creating a file that can be read by the interpreter is easy:
1. Create a new file with the file ending of .solo
2. Type :
  ```
  % My first SOLoP program %
  8 4 / !
  ```
3. Compile the .solo file using either compile.exe, or Python
After having done that, '2' should be printed out to your terminal. Congratulations, you created your first SOLoP program!
## Command References
| Command | Description | Example |
| ------- | ----------- | ------- |
| + | Adds together the last two numbers pushed onto<br> the stack, pushing the result onto the stack | ' 5 5 + ' --> ' 10 ' |
| - | Subtracts the last two numbers pushed onto the<br> stack, pushing the result onto the stack | ' 10 5 - ' --> ' 5 ' |
| * | Multiplies the last two numbers pushed onto the<br> stack, pushing the result onto the stack | ' 5 5 * ' --> ' 25 ' |
| / | Divides the last two numbers pushed onto the stack,<br> pushing the result onto the stack | ' 25 5 / ' --> ' 5 ' |
| ! | Prints out the last thing pushed onto the stack | ' 10 ! ' --> ' 10 ' |
| . | Prints out the last thing pushed onto the stack as<br> ASCII ( see: https://www.asciitable.com ) | ' 48 .' --> ' 0 ' |
| ? | Waits for input, tokenizing the input which may push<br> it onto the stack | ' ? ' --> ' Some Input ' |
| ~ | Pops the last thing off the stack | ' 5 3 1 ~ ! ' --> ' 3 ' |
| : | Duplicates the last thing pushed onto the stack,<br> pushing it onto the stack | ' 5 : / ' --> ' 1 ' |
| ; | Swaps the last thing pushed onto the stack with<br> the second to last thing pushed onto the stack | ' 4 8 ; / ' --> ' 2 ' |
| @ | Used to create procedures | ' @name { data } ' |
| & | Used to check if the last number pushed onto the<br>stack is the same as the condition | ' &0 ' |
| # | Used to check if the last number pushed onto the<br> stack is not the same as the condition | ' #0 ' |
| > | Used to roll the stack down once | ' 1 2 3 > ' --> ' 3 1 2 ' |
| < | Used to roll the stack up once | ' 1 2 3 < ' --> ' 2 3 1 ' |
| % | Used to denote a comment | ' % Something something % ' |
## Advanced
The following are quick references for more advanced topics
### Procedures
Procedures are pieces of code that can be called by a given name. A procedure is started with the '@' command, followed by the name of the procedure, then the commands the procedure is to execute, and finally closed using a '}'. Example:
```
@procedure_name { 5 5 + ! } % The first brace is not required %
```
Procedures are then called by simply calling them by name, as such:
```
procedure_name
```
Which would print out ' 10 '
### Conditionals
Conditionals are used to check if the last thing pushed onto the stack is equal to a predicate. There exist two types of conditionals:
- & : If the last thing pushed onto the stack is equal to the predicate, execute the next command
- \# : If the last thing pushed onto the stack is **not** equal to the predicate, execute the next command
Conditionals are denoted as such:
```
#0 % If the last thing pushed onto the stack is not zero %
&0 % If the last thing pushed onto the stack is zero %
```
As such, depending on if the conditional evaluates to true, the next command will/will not be executed

For more examples and trick see the sl.solo file, which contains useful procedures
## Socials
If you have any questions, you can contact me here:
- Twitter: @ChimneyEggs
- Gmail: chimneysandeggs@gmail.com
