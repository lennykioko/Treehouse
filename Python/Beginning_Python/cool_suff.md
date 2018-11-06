# Cool Python stuff
### Printing multiple strings.
```python
print("I am", "awesome") # I am awesome (automatically adds a space).
```

you can multiply strings `"!" * 120`.

### Getting the previous result from the Python REPL using the underscore( _ ).

```python
>>> 237 * 765
181305
>>> _
181305
>>> float(_)
181305.0
```

### Additional string methods.

```python
quote = "a man who never made a mistake never tried something new"

quote.title() # "A Man Who Never Made A Mistake Never Tried Something New"

quote.capitalize() # "A man who never made a mistake never tried something new"
```

### String formatting a variable.

```python
phrase = "Thank you {} for your ${} business"

phrase.format("lenny", "120.00") # "Thank you lenny for your $120.00 business"
```

### Booleans.

`bool(0)` and `bool("")` evaluate to False since they are falsy values.

when chaining booleans e.g. `True and True and True`, they are evaluated from left to right, so the first two evaluate to `True` and then it is `True and True`.

`and` works with `both`, `or` works with `either`.

For you to get `True` with `and`, `both` of them have to be `True`.

For you to get `True` with `or`, `either` has to be `True`.

You can also use parenthesis when working with Booleans.

`(True and True and True) and not (False or True)`

First get values in parenthesis, starting form left to right(inside the parenthesis)

and then not negates the value, and then you get `True and False`

`has_kids = True`

`is_smoker = True`

so, if you want someone with kids and does not smoke you just do:
 `if has_kids and not is_smoker:` (not true is false)


Shift + <- -> - highlight text

### Error Handling

creating expceptions = `raise Valuerrror("Invalid input")`

```python
except Valuerror as err:
    print(err)
```

## Lists

When you type `import this` in the REPL you get the Zen of Python.

To add a list onto another do: `list1.extend(list2)` - modifies list1

To concat two lists without modifying the initial ones just use +
`new_list = listt1 + list2
`

To open a Python REPL interactively, you do, `python -i file.py`

`del` removes a refrence to an object in memory but does not entirely get rid of the object, as in if two labels refrenced the same object and you did `del label1`, the refrence for `label2` will still work as normal.

pop actually removes the object and you can specify the index of the item to pop e.g. `list.pop(2)`

when looping over a list eg name in names, name remains equal to the value of the lastly looped over item in the list.

When your function needs to modify someone's inputted list e.g for display purposes you can create a copy of his input like so:

```python
my_copy = user_list.copy()
suggested = my_copy.pop(0)

for taco_joint in taco_joints.copy():
        if "taco" not in taco_joint.lower():
            taco_joints.remove(taco_joint)
    return taco_joints
```

Modifying a list while looping through it is discouraged as it will produce unexpected results.  This code is looping through a copy and then modifying the original.

`string.split(", ")` returns a list of the string with each item separated by the delimeter specified
`", ".join(list)` returns a string of the list separated by the delimeters provided

## Understanding dunder main

dunder stands for double under (score)

`if __name == "__main__"` - checks if the file is run directly and is not being imported.

## Python collections

### Lists
you can use extend with non-list items (iterables e.g strings)

```python
 a = [1, 2, 3]
 a.extend("abc")
 a # [1, 2, 3, 'a', 'b', 'c']
```

`.append(value)` - Add a new value onto the end of a list.

`.extend(iterable)` - Make a list longer by adding on the members of another iterable.

`.insert(index, value)` - Add a value to a list at a particular index.

You can, of course, also add lists together with the + operator. To do this in place, you'd use the increment operator +=.


`del` - A keyword for removing items from iterables or deleting whole variables.

`.remove()` - A list method that removes items from a list by their value.

`.pop()` will remove and return the last item from a list.

`.pop(index)` will remove whatever item is at index, assuming something is.

If there's nothing left in the list, or the provided index isn't available, .pop() will raise an IndexError.

`slicing [1:5]` = beginning, upto but not including

even if the ending index does not exist, slicing is intelligent and will go to the end of the list

`list[2:99999]` - it will just go to the end of the list

`list[:]` - makes a copy of the list

when you use the negative indeices, the default direction is still left to right, it is only changed whe you also change the step to a negative.

so, to get the second last and last item you do

`list[-2:]`

### Dictionaries

to update( modiy/add) multiple key-value pairs in a dictionary at once you can do:

`dictiionary.update({key1: value1, key2: value2})`

To overcome the need to pass things in order in the .format use:

```python
print("Hi, I'm {name} and I love to eat {food}!".format(food="tacos", name="Kenneth"))
```

`.keys()` is for specifically getting the keys in a dictionary and will optimize looping over a dict with many records e.g. 100+ keys


for key in dictionary.keys() returns an iterable of type `dict_keys`

for value in dictionary.values() returns an iterable of type `dict_values`

for item in dictionary.items() - returns a `tuple` with key-value pairs


### Tuples

its the comma rather than the brackets that actually make a tuple as in `my_tuple = 1,` will create a tuple while `my_tuple = (1)` won't. However, it's good practice to include the brackets as it makes it more obvious.

to use the tuple keyword pass in an iterable e.g a list

Tuples are immutable but you can change mutable objects e.g. lists that are inside a tuple.

tuple swapping  `a, b = b, a` - tuples allow us to swap values without the need of creating a new third variable (c).

`*args` is actually unpacking a tuple.

```python
for index, letter in enumerate(alphabet, start=1):
    print("{} -- {}".format(index, letter))
```

- we do plus one to start a as number 1 instead of 0
- leveraging on unpacking of tuples

If you know you'll get back multiple values and you don't care about one of them, assign it to _. For example:

`for index, _ in enumerate(my_list):`

The list item won't be available in the loop but you'll still have the step count.

Since dict.items() gives us a list of tuples, we could do this with unpacking a single variable into str.format().

```python
for group in my_dict.items():
    print("{}: {}".format(*group))
```

#### enumerate():

```python
 my_list = [5, 2, 4, 1, 3]
 for index, value in enumerate(my_list):
    print("{}: {}".format(index, value))
```

We have the same ability here since, again, we're getting a list of tuples.

```python
for group in enumerate(my_list):
    print("{}: {}".format(*group))
```

### Sets

`set()` - empty set, `{}` - empty dictionary

`set([1, 3, 5])` and `{1, 3, 5}` - both create a set

`my_set.add(item)` - appending new item to a set.

`my_set.update({2, 23}, {3, 39})` - you can use update to add (even multiple) sets onto another set

`my_set.remove(item)` - will raise a KeyError if item does not exist

`my_set.discard(item)` - will do nothing if item does not exist.

`my_set.pop()` also exists.

`set1.union(set2)` or `set1 | set2` - joins the two sets without modifying them `.update()` will modify

`set1.difference(set2)` or `set1 - set2-` finds what is in set1 but not in set2 - finds what is unique in set1

`set1.symmetric_difference(set2)` or set1 ^ set2 - items unique to both sets in order. (not shared)

`set1.intersection(set2)` or set1 & set2 - items in both sets. (common)

`isdisjoint(other)`
Return True if the set has no elements in common with other. Sets are disjoint if and only if `their intersection is the empty set.`

`issubset(other)`

 `set <= other` - Test whether every element in the set is in other.

`set < other` - Test whether the set is a proper subset of other, that is, `set <= other and set != other.`

`issuperset(other)`

`set >= other` - Test whether every element in other is in the set.

`set > other` - Test whether the set is a proper superset of other, that is, `set >= other and set != other.`

`copy()`
Return a new set with a shallow copy of s.


`random.choice(items)` will randomly pick an item for you in an indexed iterable e.g a `tuple` or a `list`



`random.sample(iterable, no. of options needed)` - ensures that the random values you get do not overlap.
### OOP

Inside of the class, variables are called `attributes`.

Whenever we call a class, it creates an instance. Each instance has full access to the all of the attributes and methods of the class.

`new_instance = NewClass()`

`new_instance.name_method()`

`self` refers to the instance of the class that is calling the method.

actually, instance.method() returns the same result as ClassName.method(instance).

if you have `**kwargs` in `__init__` you can do

```python
for key, value in kwargs.items():
  setattr(self, key, value)
```

Python is very explicit. If I don't do something explicitly,Python doesn't do it at all.

in legacy Python, every new class had to explicitly inherit from class Object but in Python 3 all classes do so automatically.

calling super inside the __init__ of the child class

`super().__init__(name, **kwargs)`

super, followed by the name of the method, pass in the parameters expected by the superclass's method but you do not pass self.

### video included in repo
Captures:
- loosely-coupled codekeyword arguments - arguemnts with a dafault value specified e.g

`def __init__(self, name="lenny")`.

- inheriting from multiple superclasses.

You can use `class.__mro__ `to look at your class's method resolution order (MRO) if you're curious. Or use the `inspect.getmro()` function with your class to get the same information. This can be really handy if you're not sure what order the classes are being assembled.

When you're using multiple inheritance, `super()` calls become really important. They let things like `__init__ `travel all the way up the chain to make sure the class has all of the bits and pieces that it needs.

### Handy Class methods

`isinstance('a', str)`

you can pass multiple values like so:

`isinstance(5.2, (int, float))` -> is it an integer or a float


`issubclass(childclass, parentclass)` -> True

```python
from thieves import Thief

kenneth = Thief()  # Thief inherits from Character
type(kenneth) # <class 'thieves.Thief'>
kenneth.__class__ # <class 'thieves.Thief'>
kenneth.__class__.__name__ # 'Thief'
```

`isinstance(<object>, <class>)` - This function will tell you whether or not   `<object>` is an instance of `<class>`. If it could be an instance of several classes, you can use a tuple of classes like so: `isinstance(<object>, (<class1>, <class2>, <class3>)).`

`issubclass(<class>, <class>)` - This function will tell you whether or not one class is a descendent of another class. Just like `isinstance()`, you can use a tuple of classes to compare against.

`type(<instance>)` will give you the class for an instance, as will `instance.__class__`. Neither of these is particularly useful.`

overriding Python's magic method `__str__ `allows you to change how the response of print an instance looks like

`__str__` - Control how your instances turn into strings.
`__int__` - Control `int()` conversion.

`__add__`, `__radd__` and `__iadd__` are some handya mathy magic methids but you hardly use them, know they exist.

you can define your own `__len__`, to allow getting the length of an instance of a class you've created.

`__contains__` is for checking is an item exists in an instance of a class.

`__iter__` is fpr looping over iterables.

yield is like return but it returns something and then continues with the execution.

#### yield

Briefly, yield lets you send data back out of a function without ending the execution of the function. Here's an example:

```python
def get_numbers():
    numbers = [4, 8, 15, 16, 23, 42]
    for number in numbers:
        yield number
```

If we used this function, with something like

`numbers = get_numbers()`

, we'd have a generator object. This is a special kind of object that has a value, a pointer to the current index, and a `__next__` method (ooh, special method!) that knows how to get the next item from the iterable. We can do `next(numbers)` and we'd get 4, then 8, then 15, and so on.

Since we're just returning values from an iterable, we can use yield from to skip the entire for loop:

```python
def get_numbers():
    numbers = [4, 8, 15, 16, 23, 42]
    yield from numbers
```

if you are customizing a mutable datatype e.g. list you modify `__init__`, if you are customizinfg an immutable datatype e.g. string/tuple you use `__new__`.

`__new__` does not take `self` as a parameter.

class methods work on the class rather than the instances of the class.

```python
for _ in range(5):
    pass
```

you want to loop but you have no use for the variable, so rather than use x and then have it unused you use the undescore which lets python know you do not have use for the variable created as you loop.

instance methods ndio opposite ya class methods

classmethods can be considered to be constructors.

A staticmethod is a method that doesn't require an instance (self) or a class (cls). So they belong to a class because, logically, they belong there. Most of the time, though, you're better served by just creating a function in the same module as your class.

So, would it be possible to do create_bookcase without it being a classmethod? Yes and no. We could write the exact same method with a few differences, like using self instead of cls, and then leave off the decorator. We'd have to create an instance of the class first, though. It'd look something like this:

```python
def create_bookcase(self, book_list):
    for author, title in book_list:
        self.append(Book(author, title))
    return self
```

We could leave off that last line, too, but it's generally a best practice to always have functions and methods return. Our use of it becomes a little weird to write out, though.

```python
>>> Bookcase().create_bookcase([("Eric Matthes", "Crash Course Python")])
```

We have to create the instance first, with `Bookcase()` and then call the method. By using a class method, we move the instance creation into the method where it makes more sense. It's a small and fairly subtle design decision but it makes for a nicer interaction in the end.


Python OOP has the motto 'we are all adults here' so we do not hide attributes or methods as much as other languages do.

by pre-pending an attributes or a method with an underscore(`_dontUse`), you let developers know that that method should not be used.

single underascore tells people not to use it but to lock people out use the double underscore (`__name`, def `__method`). Unless someone gets past Python's name mangling by accessing the new allias name outputted in `dir()`, you can be sure the attribute/method is locked away from the outside world.

therefor, There is no foolproof way of protecting your code from outside use in Python.

you can decorate a method with the @property decorator and therefore you access it as a decorator

```python
class Circle:
    def __init__(self, diameter):
        self.diameter = diameter

    @property
    def radius(self):
        return self.diameter / 2

cr = Circle(10)
print(cr.radius) # 5.0
```

however, you casnnot re-assign cr.radius like so `cr.radius = 10` or call it as a method `cr.radius()`.

to be able to re-assign you need a setter method

```python
@radius.setter
def radius(self, radius):
    self.diameter = radius * 2
```

immediately after the @, you should include the name of the method you want to set and also remember to name the method exactly as the other one.

you can do:
```python
class Hand(list):
    def __init__(self, size=5, die_class=None, *args, **kwargs):
        if not die_class:
            raise ValueError("You must provide a die class")
        super().__init__()
        for _ in range(size):
            self.append(die_class())

my_hand = Hand(die_class=D6)
```
The variable passed in die_class is used in `die_class()`, as in you can use variables to act like placeholders even in class instantiation.


Are you confused by how we're using the die_class argument? `Functions` and `classes` are `first-class citizens` in Python which means we can pass them around and use them as values just like we would any other variable. That means we can point a variable or parameter at a class or function and then call that variable just like we would the original class. Here's another example:

```python
class Car:
    pass

class Van:
    pass

class Motorcycle:
    pass

def vehicle_factory(cls, count):
    for _ in range(count):
        yield cls()
```

Now we could make any number of Car, Van, or Motorcycle instances that we want (and, notice, it's a generator function since we're using yield; if our vehicle manufacturing required a lot of memory, we could still be polite to other processes and not tie up all of the RAM with our factory). We'd do this with code similar to

```python
cars = vehicle_factory(Car, 50)
vans = vehicle_factory(Van, 10)
motorcycles = vehicle_factory(Motorcycle, 100)
```

Each time the for loop executes, it finds the class that was passed in and creates an instance of it. This ability of Python makes for really flexible code.

We could abstract our scoresheet further so we could reuse it in other games. We'd probably do this by creating a way to plug scoring categories into the class, probably through `mixins` (small classes, like our Agile class, that don't have a lot of value outside of being used with another class).


##  Write better Python

PEP - Python Enhancememtn Proposal

top-level functions - functions not inside a class or another function.

You can also check your code in the terminal by using `flake8 <script_name.py>.`

You can read PEP 20 online or by running `import this` in your Python shell.

You should not have to read the source code to understand what the library does, that's the work of docstrings.

docstrings can be handy to developers using your code since if they do `help(your_method)` they can easily get the docs.

### logging

like printing but does not throw output to the terminal.

level - The level that you want to start logging messages at. Any message at this level or above will be logged.


Logging Levels: CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET

```python
import logging

logging.basicConfig(filename="app.log", level=logging.debug)
logging.info("variable: {}".format(value))
```
### pdb - Python Debugger

```python
import pdb
pdb.set_trace() # at the point you want to  go line by line debugging.
# n for next - no wonder you should avoid single name variables
# c for continue file execution as usual

# the only time you can validly use a semi-colon in python

import pdb; pdb.set_trace()
```

Updating a script while PDB is running will not update the version in your PDB console. PDB doesn't magically reload (it would lose its place if it did).


### Dates and Times

```python
from datetime import datetime, timedelta

now = datetime.now()

# you only replace the relevant ones in your particular case.
now = now.replace(hour=3, minute=0, second=0, microsecond=0)

# alterantively you could create a datetime object like so:
birth_time = datetime(1999, 2, 7, 3, 0, 0, 0)


# when you subtract times you get a timedelta object with:
# days, seconds, microseconds
duration = datetime.now() - now

# to figure out the methods you can call on an instance do:
print(dir(duration))

duration.days
duration.seconds
duration.microseconds
duration.total_seconds

# also:
now.year
now.month
now.day
now.hour


hours_worked = round(duration.seconds/3600)

# creating a timedelta
timedelta(hours=5)

# adding a timedelta to a datetime object
now + timedelta(days=2)

# moving back in time
now - timedelta(days=7)

# get date only
now.date()

# get time only
now.time()

hour = timedelta(hours=1)

work_day = hour * 8 # you can carry out mathematical operations on timedelta

start_time = datetime(2018, 10, 21, 8, 30)
EOD = start_time + work_day
```

timedelta objects represent gaps in time. They are returned when you subtract one datetime from another. They can also be assigned to a variable and then used to augment datetime objects.

`.today()` is very similar to `.now()` with the difference being that you can specify the time zone in `.now()`

`today.weekday()` - returns int with Monday as 0.
`today.timestamp()`

refer to this link on string formatting datetime objects:

`https://docs.python.org/3/library/datetime.html?highlight=datetime#strftime-and-strptime-behavior`

```python
now.strftime("%m/%d/%y") # datetime object to string

datetime.strptime(2015-04-07, "%Y-%m-%d") # create a datetime object from a string.
```

strftime - Method to create a string from a datetime

strptime - Method to create a datetime from a string according to a format string

### timezones

datetime objects with tzinfo are considered aware cause they are aware of timezones and can be converted to time in different timezones, the others are known as naive and raise an error when you try converting to another timezone.

```python
aware_time = datetime.datetime(2014, 4, 21, 9, 0, tzinfo=pacific)
mumbai = datetime.timezone(datetime.timedelta(hours=13))
aware_time.astimzone(mumbai)
```

`timezone` - datetime type that holds an offset from UTC and allows us to move a datetime around the world

`astimezone` - method for converting an aware datetime to another timezone

use `pytz` to make your dealing with timezones easier.

feel free to revisit the course on dates and times in Python, esp. the part on timezones.


