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