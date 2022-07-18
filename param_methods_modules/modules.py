# modules = a file containing python code. May contain function, classes, etc.
# used with modular programming, which is to separate a program into parts

#import messages as msg # created module must be in the same dir
                       # (optional) "as msg" we give a name our module to simpify its usage

#msg.hello()            # using our functions after import
#msg.bye()

#from messages import hello,bye  # another way of importing
                                # or we can use "*" for importing all functions, but its dangerous if module is big
                                # now we can just use function names

#hello()
#bye()

# list of modules existing in python
help("modules")
