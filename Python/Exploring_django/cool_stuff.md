You can specify the app when migrating

`python manage.py makemigrations [app]`

`python manage.py migrate [app]`

`Model.create()` will save an in-memory instance of a model to the database and return the newly-created object.

`Model.filter(attribute=value)` will get a QuerySet of all instances of the Model that match the attribute values. You can change these values with other comparisons, too, like gte or in.

`STATICFILES_DIRS` is a setting for where to find static files. These files will either be served during development or will end up being collected by the collectstatic command during deployment.

`staticfiles_urlpatterns()` is a function that returns the URL patterns for static files based on DEBUG and a few other settings. You import it from django.contrib.staticfiles.urls.

`{% load static from staticfiles %}` - The way to import the {% static %} tag for use.

`{% static "<path/to/asset>" %}` - How to use the {% static %} tag to properly point to a static asset.

An inline is a smaller form inside of a larger form. The smaller form represents a related record in the database.

`StackedInlin`e is an inline where each field takes up the full width of the form. Fields are stacked.

`TabularInline` is an inline where each field is part of a single row for the form.

`{% for step in course.step_set.all %}` Notice that we don't use the () on all(). You don't call functions in Django's template tags, the template engine will handle that for you.

Also, step_set is automatically generated from the foreign key. Handy!

`Model.get(attribute=value)` lets you get a single Model instance by a given attribute's value.

Here is more info on `prefetch_related` and `select_related`. Don't bother too much with these until you're comfortable with Django's ORM.

```python
class Meta:
    ordering = ['field1', 'field2']
```

`get_object_or_404(Model, [selectors])` - Gets an object of Model by using whatever selection arguments have been given. For example: get_object_or_404(User, username='kennethlove') would try to get a User with an username set to "kennethlove". If that User didn't exist, a 404 error would be raised.

`linebreaks` is a filter that turns two returns in a row into HTML paragraph tags.

You apply filters to a variable with the pipe (|) character.

`blank=True` - A field can be blank (not filled in) in the admin and any other forms based on the model.

`django.utils.timezone` is Django's timezone utility that takes the TIME_ZONE setting into account.

`python manage.py test` runs all of the tests for your apps.

`django.core.urlresolvers.reverse()` takes a URL name and reverses it to the correct URL string. More information

`self.client` acts like a web browser and lets you make requests to URLs, both inside and outside of your Django project.

`assertTemplateUsed(response, 'template/name.html')` checks that a given template is used somewhere in the response of the view.

`assertContains(response, 'string')` checks that a given string is somewhere in the text of a response.

wordcount - Counts the words (defined by whitespace) in the variable.

truncatewords:X - Ends the variable after X words and appends an ellipsis if any content was cut off.

urlize - Converts HTTP(S) and email addresses into HTML anchor tags with appropriate links.

register.inclusion_tag("tag_template.html")(tag_name) or @register.inclusion_tag("tag_template.html") - Registers an inclusion tag. Inclusion tags render a template into wherever they're used.


Abstract models are awesome!!!

You'll likely find yourself using abstract inheritance more than any other kind. It's cleaner for the database, easier to wrap your head around, and generally produces faster, nicer queries.

All that's required to make a model abstract is to put abstract = True in the model's class Meta.
 verbose_name_plural lets you specify the correct plural of the model.

`from itertools import chain` - chain chains things together

`get_absolut_url()`
Since we've used it a time or two, here's more information about get_absolute_url. I definitely encourage you to provide this for every model that has a detail view.

it is good practise to have amigration for a singular change made to the db, do not pile up changes into one migration.
 

do not use MTI unless when it is necessary and you can do it cleanly.

 Multi-table inheritance, or MTI, is something you probably want to avoid most of the time. Our use of it here is solid and appropriate, but we could have solved the same issue by making the Question model abstract.
 Model forms are probably the part of the forms library that you'll use more than any other.

One of the areas of model forms that frustrates people, but is amazingly important, is the requirement to use either fields or exclude. Many people find excludes to be faster, simpler, easier because you don't have to update it every time you change your form or your model. But that's a dangerous decision to make because now any new fields will be automatically added to your displayed form. So use fields instead! Be explicit and control your fields directly by using the fields attribute!

Did you notice that commit=False? That's an amazingly handy tool with Django's model forms that allows us to get an instance of a model back. We can then use that instance to add whatever other information we need to the instance before we finally write it to the database (if we even do!).

Remember this tool because you'll use it pretty often.

I have to admit, this idea of creating form_class as non-instantiated references to form classes (that's a lot of jargon, huh?) comes mainly from Django's class-based generic views. We're not quite ready for them yet, but we'll get there.

You can create fixture data with python manage.py dumpdata and then optionally provide an app or model name. You can load that data with python manage.py loaddata and then providing the name of the fixture file. Django's documentation on fixtures is well worth a read.


`django-debug-toolbar`

Model.objects.filter(attribute__condition=value) - the underscores lets you move through db relationships

The conditions are called field lookups and there are a lot of them. The ones I seem to use the most often are gte (greater than or equal to), lte (less than or equal to), in (uh, just like Python's in keyword), and icontains (case-insensitive in for strings). I'm sure you'll find some that you love, too.

The condition can also be a related model, so, for example, if C has a foreign key to B and B has a foreign key to A, you could do: C.objects.filter(b__a__id__in=[1, 5, 10]) to get all of the C objects that have a B object with an A object whose id attribute is 1, 5, or 10. Yes, this is an over-engineered, overly-complicated scenario, but you'll be surprised how often similar things come up.

Model.objects.filter(attribute__condition=value)

The conditions are called field lookups and there are a lot of them. The ones I seem to use the most often are gte (greater than or equal to), lte (less than or equal to), in (uh, just like Python's in keyword), and icontains (case-insensitive in for strings). I'm sure you'll find some that you love, too.

The condition can also be a related model, so, for example, if C has a foreign key to B and B has a foreign key to A, you could do: C.objects.filter(b__a__id__in=[1, 5, 10]) to get all of the C objects that have a B object with an A object whose id attribute is 1, 5, or 10. Yes, this is an over-engineered, overly-complicated scenario, but you'll be surprised how often similar things come up.

If you're coding along and the form isn't submitting when you click the button, change the button's type attribute to be "submit" (or, better yet, turn it into `<input type="submit">` with all of the other classes applied).

You have to call .update() on a Queryset. You can't call it on a single model instance. You can get around this, though, by calling .update() on a .filter() or .exclude() that only has a single item in it. Not the most efficient way, though.

Docs on .create(), .bulk_create(), and get_or_create().

When you're using get_or_create(), you'll probably want to assign the object that comes back and the boolean for whether or not it was created in some variables.

course, created = Course.objects.get_or_create(title="REST API Basics") will divide up the values for you, into the two variables. If you don't need the created value, though, you can just throw it away with an underscore: course, _ = Course.objects.get_or_create(title="REST API Basics").

.values() and .values_list(). You'll use .values_list() with its flat argument set to True quite often.

.dates() and .datetimes(). These two methods will come in really handy when you need to make date-based archives.

.order_by() can accept any field or multiple fields, and can ever traverse relationships. Super handy. If you order by multiple fields, the first takes precedence and the latter fields are used only in places where the previous ones conflict.

Django's `F()` objects are a little weird to get your head around sometimes, but they very useful when you need access to values in the database in real time.

F objects are really handy when doing annotations and aggregations, which we'll get to in a couple of videos.

F objects allows updating sensitive data in your db while avoiding issues like race condition.

`.refresh_from_db()` allows you to refresh an object you have queried from the db.

Django gives us two really handy, but hard to grasp, tools for doing logical ANDs and ORs in our queries and using the values already stored in our database fields in other queries.

Django's Q() object documentation.

check out the Django docs for aggregations and annotation.

You can use F() objects in your aggregations and annotations if you need things to be more up-to-date or directly from the database. There are several aggregates available so be sure to look through the documentation to find the ones you need or want to use.

`.select_related()` and `.prefetch_related().`

Remember the direction each of these goes. select_related is used on the model when you have the ForeignKey field. prefetch_related is used on the model that's related to by the ForeignKey field.

prefetch_related won't always reduce the number of queries. It helps to prevent extra queries being run in your templates, though, by fetching and attaching the data before the template is ever rendered.

select_related, when used correctly, can drastically reduce the number of queries you run.

read the docs on `assertNumQueries` to test the number of queries being made on your db.

to resolve circular imports, you can create a function and then do the import in the function you want to import and then return that function.

The View class is the basis for all of the other Django class-based view classes. For the most part, it's a remarkably simple class with only a few methods. You can take a look at the class if you're curious.

Also, all CBV's use their .as_view() method in URLs, so get used to typing that. You can turn that into a variable (my_view = MyView.as_view()) and then link that in your URL but that is often seen as redundant and pointless.

The .get_context_data() method is one that you'll find yourself overriding quite often as you need to just stick one tiny thing into the context dictionary. Remember to use super() on this method, though, so you won't miss any context objects from other parts of the view.

f you need or want to get trickier with your ListView and DetailView views, you can actually programmatically define the queryset that should be used. Look into the get_queryset method if you need this functionality. I'll also cover it later on in the course.

In python, you can add parenthesis around any line, even imports and break the line into multiple lines.

`get_absolute_url`

`reverse_lazy` urlresolvers

This approach has gotten a lot better in recent versions of Django. It used to be a nightmare but now it often just works. I can't tell you how glad I am for that change!

It still isn't the best way to combine view functionality, though. Generally you'll want to combine view classes with mixins to get just the bits and pieces you need. Check out the next video for how to do that.

`LoginRequiredMixin`

Mixins, small classes that add or augment a single feature, are an excellent way to customize and modify your views.

I absolutely love mixins for class-based views and find them to be the right balance of customization bonuses versus code and mental work.

If you want to know more about mixins, you can read the official guide to them or check out django-braces for example code.

Django REST Framework's ModelSerializer class and how to use it to automatically turn models into resources.

models to good JSON objects

If you looked at the documentation for ad hoc viewset methods, you might be confused by the use of @detail_route. REST framework offers two decorators for ad hoc methods, @list_route and @detail_route. @list_route might seem to make more sense because you are, in fact, returning a list. The main difference between the two decorators, however, is that @detail_route is designed to receive a primary key argument. You need the primary key of the current course to be able to filter the reviews, so you'd use @detail_route instead of @list_route.

Speaking of documentation:

Routers
Viewsets

Throttling is restricting access to the api e.g. 5 requrests per minute

if you have a validator in your serializer for a field in your model with blank=True, the validator will not fire until a value is provided in that field, as in hiyo validator haina kimbelembele.

`validator.ValidationError`

import `Avg` from django to help in computing averages.

SerializerMethodfields - a method that will give a value that can be used as afield in your serializer.

doing `round(num * 2) / 2` - ensures you get values that are perfectly multiples of 5 i.e you cannot get 1.83 you instead get 1.5

using SerializerMethodfields is not very effecient since every time a request is made you query and then do some calculations, this will be a inefficient as you scale, alternativley, have an average_count field in your model and have a signal to update it once a new rating is added.

Authentication - Identifying a user, often done through a username and password combination.

Authorization - Verifying that an authenticated user has permission to perform an action.

Django's section on logging users in is definitely worth a read, especially for some of the more behind-the-scenes parts of using login() and authenticate(). Also read about the authentication views.

The logout function is your best bet for logging a user out.

Signing users up can be a very specific thing for your site, so be sure to make that process fit your site. django-registration is a very popular package for customizing the registration workflow and one I definitely recommend checking out.

If you'd like to do authentication and registration through third-party sites, let letting a user sign up with their Twitter account, check out django-allauth or python-social-auth.

One of the best things about this "I forgot my password" workflow is something you might not think about: it's done through email so people can't easily reset your password out from under you. I know this isn't an uncommon feature, but it's still a nice thing to have.

If you want to know more about Django's email backends, check out the doc

The docs for creating custom users models are really good and you should read through them even if you're going to use the standard user model. You'll see a bit more about how all of the pieces fit together.

`normalize_email` and `set_password`  really come in handy

image uploads in Django

Permissions control what users are allowed to do.

Permissions get into one of the hairier parts of Django, the contentypes framework. Have a look through the contenttypes docs if you want to know more. In short, though, it's a model that holds a reference to every non-abstract model in your project.

The PermissionRequiredMixin is from Django itself, and it only checks for a certain permission. If you need to check for multiple permissions, django-braces offers a MultiplePermissionsRequiredMixin.

Checking {{ perms }} in templates is a great way to show and hide bits and pieces based on what a user is allowed to do. You shouldn't show them buttons they can't actually click!

You can also check has_perm or has_perms on a user model, too, to see if they have the appropriate permission for a bit of logic.

For row-level or object-level permissions, django-guardian is a great project to check out.

