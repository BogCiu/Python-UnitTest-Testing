# Python-UnitTest-Testing
Learning to use the 'unittest' Python module

main file contains a coding challenge i had to do for a previous interview (in C++)
It had a very bad "presentation of the rules" so hopefully the ones below are explained well enough

  - input is an list of different types (integers and characters - in Python, this obviously is just a string of length 1)
  - go through the elements of the list from the beginning to end
  - whenever you find a character (for simplicity, it's always the same, "E"), remove the LOWEST value in the list so far
  - at the end, the output has to be all of the "removed" elements

**Additional rule, the program never gives you a "character" if you're lacking an integer to "remove"**

test file has 3 test cases for this code

TODO:
  - add testcases for different error types 
    (function uses min() function that can only take in numbers and strings. What happens if i input a "None" type or an different type)
    (need to handtle the TypeError in that case)
  - for learning purposes, use a SetUp() and TearDown() function
