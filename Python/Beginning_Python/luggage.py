def packer(name="User", **kwargs):
    # takes a list of parameters and packs them into a dict
    print("{} owns the following: {}".format(name, kwargs))


packer(name="Lenny", car="Range", bike="Honda", house="Mansion")


# def unpacker(name="User", profession="dev"):
#     print("{} is a great {}".format(name, profession))

# name_career = {"name": "Jerry", "profession": "Engineer"}

# unpacker(**name_career)

# # alternatively
# unpacker(**{"name": "Jerry", "profession": "Engineer"})
