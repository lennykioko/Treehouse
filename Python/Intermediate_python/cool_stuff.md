### Regex
```python
import re

file = open("file.txt", encoding="utf-8")
data = file.read()
file.close()

serch_term = r'Love'
print(re.search(search_term, data))
```
`r` tells python it's a raw string and saves us from work adding backlashes.

`open()` - Opens a file in Python. This won't contain the content of the file, it just points to it in memory.

`.read()` - Reads the entire contents of the file object it's called on.

`.close()` - Closes the file object it's called on. This clears the file out of Python's memory.

`r'string' `- A raw string that makes writing regular expressions easier.

`re.match(pattern, text, flags)` - Tries to match a pattern against the beginning of the text.

`re.search(pattern, text, flags)` - Tries to match a pattern anywhere in the text. Returns the first match.

### A better way to read files
If you don't know the size of a file, it's better to read it a chunk at a time and close it automatically. The following snippet does that:

```python
with open("some_file.txt") as open_file:
    data = open_file.read()
```

`The with causes the file to automatically close once the action inside of it finishes. And the action inside, the .read(), will finish when there are no more bytes to read from the file.`

Why didn't I cover this in the video? There's more going on here, behind-the-scenes, and I think it's better to know the long way first.

parenthesis are used to represent groups in regex, so you need to escape them inside the raw string using a backlash like so `r"\(d-\d\)"`.

### Regex characters

`\w` - matches an Unicode word character. That's any letter, uppercase or lowercase, numbers, and the underscore character. In "new-releases-204", `\w` would match each of the letters in "new" and "releases" and the numbers 2, 0, and 4. It wouldn't match the hyphens.

`\W` - is the opposite to `\w` and matches anything that isn't an Unicode word character. In "new-releases-204", `\W` would only match the hyphens.

`\s` - matches whitespace, so spaces, tabs, newlines, etc.

`\S` - matches everything that isn't whitespace.

`\d` - is how we match any number from 0 to 9

`\D` - matches anything that isn't a number.

`\b` - matches word boundaries. What's a word boundary? It's the edges of word, defined by white space or the edges of the string.

`\B` - matches anything that isn't the edges of a word.

Two other escape characters that we didn't cover in the video are `\A` and `\Z`. These match the beginning and the end of the string, respectively. As we'll learn later, though, `^` and `$` are more commonly used and usually what you actually want.


you can multiply strings and integers to create your pattern. For example: `r"\w" * 5` would create `r"\w\w\w\w\w"`.

`.search()` returns the first result only, to find all results use `.findall()`.

`\w{3}` - matches any three word characters in a row.

`\w{,3}` - matches 0, 1, 2, or 3 word characters in a row.

`\w{3,}` - matches 3 or more word characters in a row.There's no upper limit.

`\w{3, 5}` - matches 3, 4, or 5 word characters in a row.

`\w?` - matches 0 or 1 word characters.

`\w*` - matches 0 or more word characters. Since there is no upper limit, this is, effectively, infinite word characters.

`\w+` - matches 1 or more word characters. Like *, it has no upper limit, but it has to occur at least once.

`.findall(pattern, text, flags)` - Finds all non-overlapping occurrences of the pattern in the text.

### sets

`[abc]` - this is a set of the characters 'a', 'b', and 'c'. It'll match any of those characters, in any order, but only once each.

[`a-z], [A-Z], or [a-zA-Z]` - ranges that'll match any/all letters in the English alphabet in lowercase, uppercase, or both upper and lowercases.

`[0-9]` - range that'll match any number from 0 to 9. You can change the ends to restrict the set.

and then, you do not need to repeat a charactear in a set, so lets say you want a set for treehouse you cansimply do: `[trehous]` - e is already captured.

to ignore case, use the flag `re.IGNORECASE` the shorthand for this is `re.I`

use the `re.VERBOSE` (shorthand `re.X`) flag if your regex spans multiple lines and you do not want it to affect the regex.

to use two flags at the same time, separate the flags with a pipe  `re.I|re.VERBOSE`

`^` is for ignore the the following characters.

writing your regex over multiple lines, surrounded by three `"` and with comments makes it easy to think about and also comment on the logic of your regex.

`[^abc]` - a set that will not match, and, in fact, exclude, the letters 'a', 'b', and 'c'.

`re.IGNORECASE or re.I `- flag to make a search case-insensitive. re.match('A', 'apple', re.I) would find the 'a' in 'apple'.

`re.VERBOSE or re.X` - flag that allows regular expressions to span multiple lines and contain (ignored) whitespace and comments.

`([abc])` - creates a group that contains a set for the letters 'a', 'b', and 'c'. This could be later accessed from the Match object as .group(1)

`(?P<name>[abc])`- creates a named group that contains a set for the letters 'a', 'b', and 'c'. This could later be accessed from the Match object as .group('name').

`.groups()` - method to show all of the groups on a Match object.

`re.MULTILINE or re.M` - flag to make a pattern regard lines in your text as the beginning or end of a string.

`^`- specifies, in a pattern, the beginning of the string.
`$` - specifies, in a pattern, the end of the string.

you can used named groups by having `?P<name>` and then you can use `.groupdict()` to receive the result as a dictionary.

`re.complile()` lets you save your regex in ready to use state, mind you you do not compile with the data you are matching against. You then search by passing the compiled one and the data you are searching in as arguments in the regex method e.g. `re.search(compiled_regex, data)` N:B flags are specified when you do the compile.

and you can do an easier thing:

`compiled_regex.search(data)`

`.finditer()` is handy - read the docs

`re.compile(pattern, flags)` - method to pre-compile and save a regular expression pattern, and any associated flags, for later use.

`.groupdict()` - method to generate a dictionary from a Match object's groups. The keys will be the group names. The values will be the results of the patterns in the group.

`re.finditer()` - method to generate an iterable from the non-overlapping matches of a regular expression. Very handy for for loops.

`.group()` - method to access the content of a group. 0 or none is the entire match. 1 through how ever many groups you have will get that group. Or use a group's name to get it if you're using named groups.

The `re.MULTILINE` flag makes what change to how our pattern matches strings? - Newlines are treated as individual strings

How would I get the contents of the group named email from my match object? - `match_object.group('email')`

### File I/O

opening a file that does not exist in write/append mode will automatically create it.

the reason there is no error as a result of not closing a file when done is because garbage collection comes to your rescue, however it is good practise to be expplict and close the file.

```python
with open('file.txt', 'a') as file:
    file.write('something')
```

with provides a context manager in that, the file variable only exists within that block, outside the block, file does not exist and it will automatically close the file once its execution ends.

The two most common modes or flags for writing are "w", for truncating and then writing, and "a" for appending to the file.

read mode is the default so `open('file.txt')` will open the file in `r` mode.

`python read.py milk` - after python the file name is `argv[0]` and then everything else follows `argv[1]` e.t.c

`argv[1:]` - all arguements starting from index 1 onwards

python treats files as iterables so you can do:
```python
with open('file.txt') as file:
    for line in file:
    print(line)
```

you can specify the number of bytes you want to read like so:

```python
with open('file.txt') as file:
    file.read(10) # 10 bytes
```

file.read() no arguments or with a negative number e.g file.read(-1) will read the whple file.

there is a variable that acts as a pointer to the point to which we read a file, therefore if you read part of a file and then read again it will continue from where you left off, to reset this pointer you do `file.seek(0)` - resets it to the beginning, or to the 0th byte.

`file.readlines()` will treat each line as a separate entity

this will print every line character backwards:
```python
with open('file.txt') as file:
    lines = file.readlines()
     for line in lines:
         print(line[::-1])
```

`file.read(bytes=-1)` would read the entire contents of the file.

You can control the number of bytes read by passing in an integer.

`file.seek()` will move the read/write pointer to another part of the file.

`file.readlines()` reads the entire file into a list, with each line as a list item.

comma-separated value(CSV) file.

```python
import csv

with open("museum.csv", newline="") as csvfile:
    artreader = csv.reader(csvfile, delimeter=",")
    rows = list(artreader)
    for row in rows:
        print(",".join(row))
# csv.reader() gives output that is a list
```


alternatively use `csv.DictReader()` which returns dictionaries, you can specify the keys it should use as arguments to `csv.DictReader()`, if not provided it automatically picks these from the table headers.

```python
import csv

with open("museum.csv", newline="") as csvfile:
    artreader = csv.DictReader(csvfile, delimeter=",")
    rows = list(artreader)
    for row in rows:
        print(row['ManuCity'])
```

Writing to csv files:

```python

import csv

with open("museum.csv", "a") as csvfile:
    fieldnames = ["artwork", "age"]
    artwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

    teachwriter.writeheader()
    teachwriter,writerow({
        "artwork": "monalisa,
        :age": 25
    })
```

javascript object notation (JSON) files

```python
import json

with open("file.json") as jsonfile:
    art = json.load(jsonfile)
    print(art["name"])
```

`json.load()` takes a file-like input and converts it to data strucutures familiar to Python e.g. objects to dictionaries and arrays to lists.

json.loads()` is for json. load string - takes a string with embeded json and converts it intio a python object.

`json.dumps()` does the opp. of `json.loads()`

`json.dump()` does not directly create a string like `json.dumps()` does, it instead creates a more file-like object, i.e if you pass in two dictionaries, it will return a list of two JSON objects.

JSON is quickly becoming the de facto standard for Web-based communication. Most APIs expect, accept, and return JSON and many pieces of desktop software use JSON for configuration files.

### Databases

Object Relational Mapping (ORM)

We always name our Models in singular i.e `Student` and not `Students` because a model represents a single item in the database.

```python
sqlite 3 records.db
sqlite> .tables # get all tables
sqlite> select * from student # view everything in student db
sqlite> .exit # exit the sqlite shell
```

you can actually retrieve specific data from dictionaries in `.format()`
```python
print("Our top student is {0.username}".format(student))
```
since the object is at index 0, when we do `0.username` which is equivalent to `student.username`

### Python version on Mac

Type in `/usr/bin/env python` and you should get a Python shell like normal. If it says 2.7 or something other than the 3.4 you should be expecting, try `/usr/bin/env python3`. Whichever of these gets you the correct Python shell is the one you should put at the top of your file. Put it like so `#! <insert here>` after the she-bang(#!) character.

currently for me:

- `/usr/bin/env python` - python 3.6.7

- `/usr/bin/env python3` - python 3.6.7

- `/usr/bin/env python2.7` - python 2.7.10

to get an ordered dictionary you could do:

`from collections import OderedDict`

`OrderedDict` - a handy container from the collections module that works like a dict but maintains the order that keys are added

`.__doc__` - a magic variable that holds the docstring of a function, method, or class.

`sys` - a Python module that contains functionality for interacting with the system.

`sys.stdin` - a Python object that represents the standard input stream. In most cases, this will be the keyboard.

`os` - Python module that lets us integrate with the underlying OS.

`os.name` - attribute that holds a name for the style of OS

`os.system()` - method to allow Python code to call OS-level programs.

to clear the screen on Windoes and mac run:
```python
os.system('cls' if os.name == 'nt' else 'clear')
```

### Testing
doctest - A test written in a docstring.

doctest library - The built-in Python library for running doctests.

Running doctests From the command line

`python -m doctest your_script.py`

`-m` tells python  to load the doctest module

TestCase - A collection of tests

all tests in a TestCase have to start with the word test_ to be run. You can have methods that don't start with test_ for other purposes if you need them.

`setUp()` - Method that is run before each test. Use this to set up state for the tests

`assertEqual(x, y)` - Make sure x and y are equal

`assertNotEqual(x, y)` - Make sure x and y are not equal

`assertGreater(x, y)` - Make sure x is greater than y

`assertLess(x, y)` - Make sure x is less than y

`assertIn(x, y)` - Make sure x is a member of y (this is like the in keyword)

`assertIsInstance(x, y)` - Make sure x is an instance of the y class

`assertGreaterEqual(x, y)` - Make sure x is greater than or equal to y

`assertLessEqual(x, y)` - Make sure x is less than or equal to y

end of `range()` should be 1 higher than the value you wanna reach.

```python
with self.assertRaises(ValueError):
    code supposed to raise the error
```

tests that an error is raised. You need the context manager created by with.

`assertRaises(x)` - Make sure the following code raises the x exception

You can use `@unittest.expectedFailure` on tests that you know will fail

Example
```python
with assertRaises(ValueError):
    int('a')
```

### Comprehensions

#### List comprehensions:
```python
halves = [num for num in range(0, 101) if num % 2 == 0]
```

we do not have `else` since it makes it hard to read and comprehend.

```python
rows = range(0, 11)
colums = range(11, 21)

# like a cool two in one
grids = [(x, y) for x in rows for y in columns]
```

#### Dictionary comprehensions:

```python
{number: letter for letter, number in zip("abcdefghijklmnopqrstuvwxyz", range(1, 27))}

{student: points for student, points in zip(["lenny", "mark", "tom"], [122, 312, 456])}

# generate a dict with the solutions for fizz and buzz
numbers = range(0, 101)

fizbuzzes = {
    "fizz": [num for num in numbers if num % 3 == 0],
    "buzz": [num for num in numbers if num % 7 == 0]
}

# Added after understanding set comprehension which is below
fizbuzz = {num for num in set(fizbuzzes["fizz"]) & set(fizbuzzes["buzz"])}
fizbuzzes["fizbuzz"] = list(fizbuzz)
print(fizbuzzes)

```

#### Set comprehensions:
```python

# contains no duplicates
{(x + y) for x in range(1, 11) for y in range(1, 11)}
```
we do not have comprehensions for strings and tuples since they are immutable.

```python
# list comprehension
>>> [num * 2 for num in range(1, 6)]
[2, 4, 6, 8, 10, 12]

# dict comprehension
>>> {letter: num for letter, num in zip('abcdef', range(1, 7))}
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# set comprehension
>>> {num * 2 for num in [5, 2, 18, 2, 42, 2, 2]}
{84, 10, 4, 36}
```

### Decorators
functions can live inside other functions, the inner function has access to the scope of the outer one.

functions are first class objects/citizens - you can pass a function to another function and call it inside that function.

```python
def outer():
    number = 10

    def inner():
        print(number)

    inner()


outer()


def apply(func, x, y):
    return func(x, y)


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


print(apply(add, 10, 10))

print(apply(sub, 10, 10))


# closures in Python
def close():
    x = 5

    def inner():
        print(x)

    return inner  # we are returning the function, not returning the called function.

# close() basically returns a pointer to inner
closure = close()

# close() returned a pointer to inner, so closure() is basically like doing inner()
closure()

# closures with arguments
def add_to_five(num):
    def inner(): # note that num is not specified as a param here, in fact doing so raises an error but since the inner function has access to the scope of the outer, it is still able to pick up on num
        print(num + 5) # num is picked from the outer functoion
    return inner

fifteen = add_to_five(10)
fifteen()

def logme(func):
    # we import it here so that you do not have to add this import to every file in which you use the decorator
    import logging
    logging.basicConfig(level=logging.DEBUG)

    # inside inner you do whatever you wanna do and then end by returning the called function you are decorating
    def inner():
        logging.debug("You called {}".format(func.__name__)) # func is picked from the scope of logme
        return func() # call the function passed to us
    return inner # remember not to call it here

@logme
def print_4():
    print("4")

print_4()

# decorating functions that take in some arguments
def logme(func):
    import logging
    logging.basicConfig(level=logging.DEBUG)

    def inner(*args, **kwargs): # you pass in args and kwargs in innner and not in the decorator(logme)
        logging.debug("You called {} with these args: {} and these kwargs: {}".format(func.__name__, args, kwargs)) # here we want to print the actual tuple adn dictionary of args and kwargs
        return func(*args, **kwargs) # here we want to unpack the tuple and the dictionary.
    return inner

@logme
def sub(x, y, switch=False):
    return x - y if not switch else y - x # cool stuff here, putting the logic on one line

print(sub(5, 2))
print(sub(2, 8, switch=True))
```

The problem with using the decorator in this way comes when trying to get attributes of the function you've decorated, instead of getting its attributes you get hte  attributes of the `inner` function.

```python
def logme(func):
    import logging
    logging.basicConfig(level=logging.DEBUG)

    def inner(*args, **kwargs):
        logging.debug("You called {} with these args: {} and these kwargs: {}".format(func.__name__, args, kwargs))
        return func(*args, **kwargs)
    return inner

@logme
def sub(x, y, switch=False):
    """returns the difference between two number"""
    return x - y if not switch else y - x


print(sub.__name__) # returns inner instead of sub
print(sub.__doc__) # returns the docstring of inner instead of sub
help(sub) # does not return the correct help for sub

# solution one is to do this inside inner(at the end) but this is not scalable,
inner.__name__ = func.__name__
inner.__doc__ = func.__doc__

# wraps sorts all teh se issues for you and more

# Best solution
from functools import wraps
def logme(func):
    import logging
    logging.basicConfig(level=logging.DEBUG)

    wraps(func)  # Yes, decorators can take in arguments
    def inner(*args, **kwargs):
        logging.debug("You called {} with these args: {} and these kwargs: {}".format(func.__name__, args, kwargs))
        return func(*args, **kwargs)
    return inner

@logme
def sub(x, y, switch=False):
    """returns the difference between two number"""
    return x - y if not switch else y - x


print(sub.__name__) # returns sub
print(sub.__doc__) # returns the sub's docstrings
help(sub) # works as expected

# wraps solve all these and much more, use it
```


Nested function:
```python
def outer():
    number = 5

    def inner():
        print(number)
    inner()

outer()  # prints 5
```

First-class functions
```python
def apply(func, x, y):
    return func(x, y)

def add(a, b):
    return a + b

print(apply(add, 5, 5))  # prints 10
```

Closures
```python
def close():
    x = 5

    def inner():
        print(x)
    return inner

closure = close()  # closure is actually a pointer to inner()
closure()  # prints 5
```

Decorator
```python
def logme(func):
    import logging  # because we don't want to require users to import it
    logging.basicConfig(level=logging.DEBUG)

    def inner():
        logging.debug("Called {}".format(func.__name__)
        return func()
    return inner

@logme
def say_hello():
        print("Hello there!")

say_hello()  # logs the call and then prints "Hello there!"
```

### Type Hinting

dynamically typed - a variable can be assigned values different types over time e.g. an int, then an string , then a float. Python, JS, Ruby. C# and Java are the opposite to this.

Relevant resourves:

PEP 3107

PEP 484

PEP 526

The typing module

mypy, the Python static type checker


to add type hinting to this function:
```python
def add(num1, num2):
    return num1 + num2

def add(num1: int, num2: int) -> int: # specify the type with a colon followed by a space and then the type,  and then you specidfy the returned type after the arrow.
    return num1 + num2
```

there is a data type in python known as `complex` which caters for `int`, `float` and for a `complex` number which is a combination of a real number and an optional imaginery number.

```python
def add(num1: complex, num2: complex) -> complex: # allows for int, float (real numbers) and complex numbers
    return num1 + num2
```

To ensure it only works with real numbers and not with complex numbers, we could do

```python
from numbers import Real
def add(num1: Real, num2: Real) -> Real: # allows for only real numbers (int and float)
    return num1 + num2
```

The tyoping module gives us some handy tools, List, Union and Optional.
```python
# List is for lists
Ingredient: Union[int, str] # either an int or a str
Ingredient: Optional[str] # the param is optional, it can get a value of type str or even nothing at all
```
You can do this type hinting on variables too.

if you do not want to provide a default to a variable you can just specify the type and leave it that way, this makes Python look like C, ile design you need to declare types before using them but you should note that doing so does not create the variable, you have just specified the type you expect it to be.(in  Python).

```python
def __init__(title):
    self.order: str # just semantic sugar, does not create the variable
    self.title: str = title
```
For more see the file and video in this folder.


shortcut to .format:
```python
# Instead of this
"({})".format(self.condition)

# Just do this
f'({self.condition})'
```

whether to use this style is something you need to discuss with your team, but it vcan make working with a large codebase easier.

`filename.pyi` - stub files

stub files let you do type hinting in a separate file therefore not needing to add code that may be unfamiliar to other developers in your codebase. You just specify your function/class definitions, params and variables and leave out the logic.

Pycharm does the type checking for you, if you are on a different editor, use mypy.


### Functional Programming (FP)

FP is a nice super power to have in your arsenal.

Functional programming is a popular approach in a lot of languages and is even the main approach in some. If you find you like functional programming, check out the languages Haskell and Scala.

Popular approaches to programming

- Procedural programming - top to bottom exection with  a few functions mainly for repetitious tasks. Most programmers start out here.

- Object Oriented Programming - classes, methods, attributes

- Functional programming

Functional programming has some pretty important central rules that we should understand.


The rules:

- Computation is the evaluation of functions

- Programming is done with expressions

- No side-effects from computation

- Functions are first-class citizens

- Functions should be limited in scope and functionality


Functions, ideally, should only do one thing.

the `global` keyword lets you access the global scope from inside the local scope of a function.

`random.shuffle(range(05, 250))` - shuffles the list generated

global and nonlocal let you work with variables from a higher scope. You should have a really good reason before using either of these!

#### sorted()
.sort() sorts the list in place which causes a side effect, therefore, sorted is recommended since it makes a copy of the list, sorts it and then returns this copy and it therefore causes no side effect.

```python
def get_sorted_list(my_list):
    my_list.sort()  # bad idea, sorts list in place, thus causing a side effect.
    sorted(my_list)  # good idea, no side effect, sorts a copy of the list
```

when you need to tell sorted how to sort your data, by specifying the sorting criteria do:

```python
from operator import attrgetter, itemgetter
# attrgetter, itemgetter - given an object and a key/attribute name, and ask it to give you that key and it will give it to you.
BOOKS = get_books("books.json")
RAW_BOOKS = get_books('books.json', raw=True) # custom function
pub_sort = sorted(RAW_BOOKS, key=itemgetter('publish_date'))
# key is a kwarg for sorted which specifies what to use to sort the items involoved.
print(pub_sort[0]['publish_date']) # print the publish_date of the first dictionary  in sorted list
print(pub_sort[-1]['publish_date']) # print the publish_date of the last dictionary in sorted list

pages_sort = sorted(BOOKS, key=attrgetter('number_of_pages')) # we use atrrgetter since we are dealing with objects here(instances of a class which have number_of_pages as attributes)
print(pub_sort[0].number_of_pages) # print the number_of_pages attribute of the first item in sorted list
print(pub_sort[-1].number_of_pages) # print the number_of_pages attribute of the last item in sorted list

# Notice that when using attrgetter and itemgetter inside sorted, we do not have to pass in the objects(BOOKS and RAW_BOOKS) to them since sorted automatically sends the object to the key kwargs from which attrgetter and itemgetter can access it.

pages_sort = sorted(BOOKS, key=attrgetter('number_of_pages'), reverse=True) # reverse=True flips the list
```
sorted() takes an iterable to sort and returns a new list from it. If you need to customize the sorting, pass a function in as the key argument. There's an optional reverse argument that will cause the results to be reversed before they're returned.

operator.itemgetter()gets items from an object that supports that operation. We use it to get keys from dicts but it has other uses too.

operator.attrgetter() gets attributes from an object.

Wait, you didn't talk about reversed in the video!

reversed() is important but isn't all the unique or remarkable for a video right next to sorted(reverse=True) so I left it out. But good job, you, finding it here!

reversed() takes an iterable and reverses it, returning a new iterable. This new iterable has to be turned into a list/tuple/etc to get items from it by index.

#### map

map allows you to apply a function to every item in an iterable and  gives us back a new custom iterable.

It does not return a list by default, so you need to wrap the response in list() to make it a list.

```python
a = [1,2,3,4]
def double(n):
    return n * 2

doubled = list(map(double, a))
print(doubled)
```

```python
# to avoid changing the actual object, we do:
from copy import copy

book = copy(book)
```

`round(value, no. of decimal points)` e.g `round(100/22, 2)`

```python
from copy import copy

def apply_sales_price(book):
    """apply a 20% discount on the price of a book"""
    book = copy(book)
    book.price = round(book.price - book.price*2, 2)
    return book

sales_books = list(map(sales_price, BOOKS))
print(sales_book[0].price)

# as a list comprehension
sales_book = [sales_price(book) for book in BOOKS]
# map and the list comprehension are very similar in effeciency and processing time, the reason to pick map over the list comprehension is the easy readability and scalability of map as things get more complex and/or you need to nest it in other functions
```

`map()` lets us apply transformations to each item in an iterable.

map() takes a function and an iterable. The function should take a single argument. This function will be applied, in order, to each item in the iterable and the result of that function will be returned to map(). In the end, map() will return a new iterable with the mutated values.

[func(item) for item in iterable] achieves the same result, plus turns the results into a list. For simple, single-serving applications, this is often a better choice since it's often more readable at a glance.

#### filter

filter() takes a function and an iterable, it runs the function on each item of the iterable and when for a particular item it receives True it adds the item to the iterable it creates, otherwise it discards the iterable.
Just like in `map()`, if you want the output as a list, wrap `filter()` with `list()`.

```python

def is_long_book(book):
    """Is the book at least 600 pages long?"""
    return book.number_of_pages >= 600

long_books = list(filter(is_long_book, BOOKS))

# as a list comprehension
long_books = [book for book in BOOKS if is_long_book(book)]

# or

long_books = [book for book in BOOKS if book.number_of_pages >= 600]


```

Most times the convention for functions to be used in `map()` start with `apply_` and for `filter()` they start with `is_` or `are_`

`map()` and `filter()` can come in handy when you need to write re-usable code to be used for certain diffferent operations/iterables unlike the comprehension which will work with a specific iterable, the comprehension is suitable for something you just want to run once.

when you need to get the falsy values from your filter(), you could flip the logic to return True for these items or you could use `filterfalse()` instead.

`filter()` takes a function and an iterable. The function, like with `map()`, takes only a single argument and is applied to each item in the iterable. If the function returns a truthy value for the item, the item is sent back to `filter()` which, ultimately, returns a new iterable of the filtered items.

You can achieve the same effect with `[item for item in iterable if func(item)]`. Again, like with `map()`, this can be more quickly readable for small applications.

I mentioned `filterfalse()`. This function works just like `filter()` but only returns things where the filter function gives back a False or non-truthy value. You can read more in the documentation.

Since `filter()`, `map()`, s`orted()`, and friends all return iterables, we can chain them together. Chained functions resolve, or happen, from the inside out, so the innermost function runs first.

This is another reason why functions usually return a value at the end. It makes it easier to use them all together.

`any(iterable)` returns `True`if any of the items in the iterable are truthy. Similar is the function `all()`. `all(iterable)` returns `True` if all of the items in the iterable are truthy.

```python
print(list(map(titlecase, filter(has_rowland, BOOKS))))
```

```python
# first get the sales_price for each book, filter this to only those cheaper than 1000 bob and then sort them based on price.
cheap_books =sorted(
    filter(is_good_deal, map(sales_price, BOOKS))
    key=attrgetter("price")
)
```

note that the logic is executed from inside moving outwards - this is key

#### reduce

reduce lets you work through an iterable in a rcursive way:
It behaves in a way like ut has an outer variable that stores the results of the previous operation

```python
from functools import reduce
items = [1,2,3,4,5]
def product(x, y):
    return x * y

total = reduce(product, items)

# the above is a shorter way of doing
total = 1
for item in items:
    return total * item
print(total)
```
A recursive function - a fi=unction that repeatedly calls itself to get new values

```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
```

functools.reduce() takes a function and an iterable. The function, though, takes two arguments. The first time it runs, the two arguments will be the first two items in the iterable. Every time after that, the first argument will be the result of the last time the function was run. The second argument will be the next value from the iterable. When the iterable is out of items, reduce() will return whatever the function returned last.

Think about adding up all of the numbers in a column. You add the top two, then add the third number to the sum you got from the first two. Then you add the fourth number to the sum of the top three, and so on.

Calling a function over again from within itself is known as recursion and it's what makes reduce() able to do its job.

to get a function to add stuff, you could do:
```python
from operator import add
```
#### lambdas

lambdas cannot contain assignments e.g. `a = 5`

`lambda x, y: x + y` - lambda is followed by the arguments required and then the operation you want done. Lambdas have an implicit return and will return the result of the last operation evaluated.

```python
total = reduce(lambda x, y: x + y, [book.price for book in BOOKS]) # same output but we did not have to create a new function just to add two numbers together.
```
```python
filter(lambda book: book.number_of_pages >= 600, BOOKS)
```
The idea behind lambdas is that we do not need to write a function only to use it one time qnd in one location.

if you need to re-use the logic, it is better just creating a function.

lambda, like def, is the keyword that marks a new function. Lambda functions don't have to have a name, though.

Lambdas can't contain new lines (outside of containers) or assignments.

```python
from functools import reduce

strings = [
    "Do not take life too seriously. You will never get out of it alive.",
    "My fake plants died because I did not pretend to water them.",
    "A day without sunshine is like, you know, night.",
    "Get your facts first, then you can distort them as you please.",
    "My grandmother started walking five miles a day when she was sixty. She's ninety-seven know and we don't know where she is.",
    "Life is hard. After all, it kills you.",
    "All my life, I always wanted to be somebody. Now I see that I should have been more specific.",
    "Everyone's like, 'overnight sensation.' It's not overnight. It's years of hard work.",
]

longest = reduce(lambda string1, string2: string1 if len(string1) > len(string2) else string2, strings)
```
#### partial

Partial functions let us partially apply a function

functools.partial lets you preset some arguments to a function. You can then call the new function with the remaining arguments as needed. This often ends up being really handy when used with map() and filter().

```python
def mark_down(book, discount):
    book = copy(book)
    book.price = round(book.price-book.price*discount, 2)
    return book

standard = partial(mark_down, discount=.2)
half = partial(mark_down, discount=.5)

half_price_books = map(half, BOOKS) # or adding a filter;

half_price_books = map(half, filter(is_long_book, BOOKS))
```

Currying is creating new versions of a function until all of the conditions are satisfied.

Currying is a technique you don't come across in Python very often. But, thanks to lambdas, we can implement it pretty easily.

It is not commonly used, but it is good you know it exists.
