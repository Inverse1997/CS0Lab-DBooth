"""
    stdIO Lab
    ASCII Art - using literals and variables

    Updated by: Daniel Booth #FIXME1 #fixed
    Date: 08/31/2023 #FIXME2 #fixed

    This program produces an ASCII art on the console.

    Algorithm steps:
    1. use variables to store data/values
    2. Write a series of print statements to print the data/values to the console
    ASCII Art Cowboy from b'ger from ASCIIart.eu
"""

print("welcome to ASCII Art Program..\n")

print("what is your name?")
name = input("please enter your name here:")
print("Good day, Nice meeting you. "  + name)
 
#FIXED: Prompt user to enter their name and store the value into name variable using input function
#FIXED: greet the name using the variable as the following output
#must output: Nice meeting you, <name>!

 #prompt user to enter the semester and store the value into semester variable using input function
semester:str = input("what semester is this [fall/spring]? ")
print("This is " + semester + " semester.\n")
year:str = input("What year is it? ")
print("This is. " + year)
#FIXED: prompt user to enter the year and store the value into year variable using input function
#FIXED: print the year using the variable as the following output
#must output: This is 2023 year.

print("I Hope you like my ASCII art...\n\n")

cowboy = """
                '___,'
              __)____)__
                -)- )))
        ,       \=_/ \__
     __/).          )_/=\\
    /6)   \      __((_\_/\\
   /   __/ \    /_/-\o____)
  / ,_/|    \   \/  ))\\\\\\
  \_)o_'     _.-'  ,/:_/_\\    ___
       '---`' \>__/   /\\---.,/_  \\
       (      /  /  /\\        \)  \\
       |        ('  \\\        (   /
  _____/         )__\\ /       /\ (
 / _______/,_____| |_,(       /  ) )
/ (_     \  |   _/ o)  \     /_  |/
\_ /     ( '| (___/     `.__  /  '
          \ |        / _/ / _/
           \(       / /  / /
            )\     / (  ( <
         ,./_(,, ,/_|    \_/,,._
"""
print(cowboy)


String_one = ("-^-")       
string_two = ("(o_o)")
String_thr = ("<<|>>")
string_fou =  ("//\\")


print(String_one)
print(string_two)
print(String_thr)
print(string_fou)


# FIXED use variable to print the second line of the graphic
# FIXED Print the third line of the graphics
# FIXED use variable to print the fourth line
# FIXMED use variable to print the fifth line



print("\nGood bye... \n")
