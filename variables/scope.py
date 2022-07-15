# scope =   region that a var is recognised
#           A var is only available from inside the region it is created.
#           A global and a local scoped versions of a var can be created.

name = "Zhopka"         # global scop (created and available inside and outside functions)

def display_name():
    name = "Yurik"      # local scope (was created and available inside of this function)
    print(name)

display_name()

# ATTENTION: Python use local variables first
# globals used if local are not available or after them
