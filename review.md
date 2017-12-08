###################
### from exam 1 ###
###################

len(list) => returns number of items in a list

str(value) => converts a value (integer, float, boolean) to a string
int(value) => converts a value (float, boolean, string) to an integer [drops decimal]
float(value) => converts a value (integer, boolean, string) to a float [also occurs when dividing integers]

print(output, [additional outputs separated by commas], [end = ], [sep = ], [file = ])
input(prompt) => collects user input as a string

type(variable or value) => returns datatype of given variable or value

###################
### from exam 2 ###
###################

booleans => True, False
numbers => integers, floats
collections => "strings", [lists], (tuples), range()
dictionaries => {key : value}

loops => while, for /// break (breaks out of a loop), continue (continues to next iteration)
pass => empty operation

import random

random => random.randrange(low, high); random.shuffle(list)

## string operations ##
substring in string

concatenate => string + string

string.lower() => lowercase (returns; not in place)
string.upper() => uppercase (returns; not in place)
string.strip() => strips whitespace (or specified characters) from start and end (returns; not in place)
string.split() => splits string into array by delimeter (returns; not in place)
print
string.find(substring) => returns index of a substring

## list operations ##
element in list

list.append(value) => adds value to end of list (in place)
list.insert(index, value) => adds value at specified index (in place)
list.remove(value) => removes first match of value from list (in place)
list.pop(index) => removes index from list (in place)

list.sort([reverse = ]) => sorts list in place; compare to sorted(list) which returns a sorted list
list.reverse() => reverses list (in place)

list.index(value) => returns index of first match of value from list

list(collection) => returns collection (tuple, string, range, dictionary) as list (returns only keys from dictionary)

## ranges ##
range(end) => counts up from 0 /// [0, end)
range(start, end) => counts up from start /// [start, end)
range(start, end, step) => counts up from start by step /// [start, end)

## dictionary operations ##
dict.keys() => returns dict_keys object with dictionary keys (convert to list to use)
dict.values() => returns dict_values object with dictionary values (convert to list to use)
dict.items() => returns dict_items object with key-value pairs as tuples (convert to list to use)

dict.pop(key) => removes item from dictionary by key (index)

## file operations ##
f = open(filename, write || read || append) === "w" will overwrite!

# reading #
    f.read() => returns one long string
    f.readline() => returns one line at a time (moving the pointer forward)
    f.readlines() => returns a list of lines

# iterate through lines #
    f.readlines(), then through the list
    f.read().split("\n"), then through the list
    for line in f, then act on each line

# writing #
    f.write() => writes to file
    f.writelines(list) = writes a list of lines to a file

f.close() => closes connection to file

## URL operations ##
import urllib.request

conn = urllib.request.urlopen(url)
conn.read().decode("utf-8") => returns HTML from URL

###################
### for exam 3 ###
###################

## error handling ##
try: ... except Error: ...

# errors #
    AttributeError => variable.attribute, but variable doesn't have such an attribute
    SyntaxError => incorrect Python syntax
    TypeError => operation doesn't work on a variable of this type (i.e. iterating thru an integer)
    IndentationError => self-explanatory
    NameError => variable is called but not defined
    IndexError => index not in sequence or collection
    KeyError => key not in dictionary
    KeyboardInterrupt => user attempts to end program with Ctrl + C
    ImportError => package not found to import from
    EOFError => no input from input() or end of file

## PyGame ##
import pygame, gamebox

one.touches(two) => box one is touching box two
one.move_to_stop_overlapping(two) => moves box one to stop overlapping with box two
one.move_both_to_stop_overlapping(two) => moves box one and box to equally to stop overlapping

camera.clear([color]) => clears screen, optionally with a certain color
camera.draw(box) => draws object
camera.display() => makes what is currently drawn visible

timer_loop(TPS, tick function) => FPS and function to run that often

## Regular expressions ##
import re

re.compile(r"expression") => creates a compiled regular expression to use in various operations
compiled.search(string) => finds first substring matching compiled expression in string; returns match object
compiled.finditer(string) => finds all substrings matching compiled expression; returns an iterable match object containing multiple match objects
re.sub()

match.group(), match.group(0) => returns the entire substring matched with the expression
match.group(n > 0) => returns a group explicitly defined in your expression with (parentheses)
match.groups() => returns a tuple of all explicitly defined groups in your expression
