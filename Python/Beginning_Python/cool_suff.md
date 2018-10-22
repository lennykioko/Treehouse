# Cool Python stuff
### Printing multiple strings.
`print("I am", "awesome")` -> I am awesome (automatically adds a space).

you can multiply strings `"!" * 120`.

### Getting the previous result from the Python REPL using the underscore( _ ).
(are facing opp. direction for formatting reasons).

<<< 237 * 765

181305

<<< _

181305

<<< float(_)

181305.0

### Additional string methods.

quote = "a man who never made a mistake never tried something new"

`quote.title()` -> "A Man Who Never Made A Mistake Never Tried Something New"

`quote.capitalize()` -> "A man who never made a mistake never tried something new"


### String formatting a variable.

phrase = "Thank you {} for your ${} business"

`phrase.format("lenny", "120.00")` -> "Thank you lenny for your $120.00 business"

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

accessing the error message = `except Valuerror as err:`
`print(err)` -> Invalid input

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

`my_copy = user_list.copy()`

`suggested = my_copy.pop(0)`


`for taco_joint in taco_joints.copy():
        if "taco" not in taco_joint.lower():
            taco_joints.remove(taco_joint)
    return taco_joints`

Why do you think the author used the copy method in the for loop here:

Modifying a list while looping through it is discouraged as it will produce unexpected results.  This code is looping through a copy and then modifying the original.

`string.split(", ")` returns a list of the string with each item separated by the delimeter specified
`", ".join(list)` returns a string of the list separated by the delimeters provided

## Understanding dunder main

dunder stands for double under (score)

## Python collections

### Lists
you can use extend with non-list items (iterables e.g strings)

e.g.

 a = [1, 2, 3]

 a.extend("abc")

 a -> [1, 2, 3, 'a', 'b', 'c']

.append(value) - Add a new value onto the end of a list.

.extend(iterable) - Make a list longer by adding on the members of another iterable.

.insert(index, value) - Add a value to a list at a particular index.

You can, of course, also add lists together with the + operator. To do this in place, you'd use the increment operator +=.


`del` - A keyword for removing items from iterables or deleting whole variables.

`.remove()` - A list method that removes items from a list by their value.

`.pop()` will remove and return the last item from a list.

.pop(index) will remove whatever item is at index, assuming something is.

If there's nothing left in the list, or the provided index isn't available, .pop() will raise an IndexError.

slicing [1:5] = beginning, upto but not including

even if the ending index does not exist, slicing is intelligent and will go to the end of the list

list[2:99999] - it will just go to the end of the list

list[:] - makes a copy of the list

when you use the negative indeices, the default direction is still left to right, it is only changed whe you also change the step to a negative.

so, to get the second last and last item you do

`list[-2:]`

### Dictionaries

to update( modiy/add) multiple key-value pairs in a dictionary at once you can do:

`dictiionary.update({key1: value1, key2: value2})`

To overcome the need to pass things in order in the .format use:

`print("Hi, I'm {name} and I love to eat {food}!".format(food="tacos", name="Kenneth"))`

.keys() is for specifically getting the keys in a dictionary and will optimize looping over a dict with many records e.g. 100+ keys


for key in dictionary.keys() returns an iterable of type `dict_keys`
for value in dictionary.values() returns an iterable of type `dict_values`
for item in dictionary.items() - returns a `tuple` with key-value pairs

### Tuples

its the comma rather than the brackets that actually make a tuple as in `my_tuple = 1,` will create a tuple while `my_tuple = (1)` won't. However, it's good practice to include the brackets as it makes it more obvious.

to use the tuple keyword pass in an iterable e.g a list

Tuples are immutable but you can change mutable objects e.g. lists that are inside a tuple.

tuple swapping  `a, b = b, a` - tuples allow us to swap values without the need of creating a new third variable (c).

`*args` is actually unpacking a tuple.

`for index, letter in enumerate(alphabet, start=1):
    print("{} -- {}".format(index, letter))`

- we do plus one to start a as number 1 instead of 0
- leveraging on unpacking of tuples

If you know you'll get back multiple values and you don't care about one of them, assign it to _. For example:

`for index, _ in enumerate(my_list):`

The list item won't be available in the loop but you'll still have the step count.

Since dict.items() gives us a list of tuples, we could do this with unpacking a single variable into str.format().

`for group in my_dict.items():
    print("{}: {}".format(*group))`

enumerate():

 `my_list = [5, 2, 4, 1, 3]
 for index, value in enumerate(my_list):
    print("{}: {}".format(index, value))
`
We have the same ability here since, again, we're getting a list of tuples.

`for group in enumerate(my_list):
    print("{}: {}".format(*group))`


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