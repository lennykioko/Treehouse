# Exploring Flask

framework - collection of code that makes doing something simpler/easier

`pip freeze | grep Flask` - just get the result of the package specified

dunder: A quick way of saying "double underscore".

View: A view is a function that returns an HTTP response. This response has to be a string but can be any string you want.

Route: A route is the URL path to a view. They always start with a forward slash / and can end with one if you want.

global: A global is a variable that exists outside of the normal Python scopes. It is available everywhere.

query string: The part of a URL that comes after the ?. You'll notice that the information after this looks like keyword arguments.

request: request is a Flask global that represents the request that the client has made to your application. This contains things like cookies, the path, and, in our usage, the query string.

`{% block %}:` This template tag (as they're called) defines a block in a template. In templates that are extended, these areas are overridable. In templates that extend other templates, this areas will override the parent template's block.

`{% extends %}:` This template tag specifies what template is the parent of the current template. Think of it like extended classes in Python. You can have a change of extensions if you need them.

`{{ super() }}:` This function brings in whatever content was in the same block in the parent template. Very handy if you want to include the existing content but you want to insert new content before or after the old.

The static/ directory is served automatically at `/static` while you're running your Flask app.

You also don't have to use every block in every child template. If you don't specify a new version of the block, Flask will just use whatever is there in the parent template.

To avoid an exception when refrencing a key that does not exist you could use `dictionary.get("key", dafault_value)`

Response: A response is the data that the server, Flask, sends back to the client.

`make_response()`: This function generates the entire response object that'll be sent back to the client, but lets you store it in a variable for further manipulation.

`response.set_cookie()`: Sets a cookie on the response object. Takes name for the cookie and a value.

`json.dumps()`: This method turns a Python data structure (list, string, dictionary, etc) into a JSON string.

`json.loads()`: This method turns a JSON string into a Python object.

`{% for x in y %}`: You already know what for x in y: does in Python, but this is the template version. This will cause the enclosed code to be run as many times as there are things in y. Has to be followed by `{% endfor %}`.

`{% if %}`: The template version of Python's if condition. Closed with `{% endif %}`.

`flash()`: This function stores a message in the session that will self-destruct after the response is returned.

`get_flashed_messages()`: This function gets all of the flash messages stored in the session.

`app.secret_key`: This configuration attribute stores the secret key that all messages are cryptographically signed with.

`{% with %}`: The Flask template version of Python's with block. Let's you temporarily define a variable. Must be closed with `{% endwith %}`.