__doc__="""
example
=======

This is the top level of the demonstration module.  It does not really
provide any useful functionality.  It is merely here as something I can
test this tool on.  A very important requirement is that Unicode
characters are passed untouched.

Another Header
--------------

`pandoc` converts the level 1 headers to `sections` in LaTeX and the
lower level headers are subsequently lowered.  This is fine with me
because I want the API to be one chapter in my dissertation.

Subpackages
-----------

submodule
:   A submodule to test
another
:   A second submodule

Data
----

C
:   Speed of light in vacuum µm s⁻¹

"""

def spam(arg):
    """
    Spam the standard output

    Enter an infinite loop and simply print a bunch of junk to the
    screen.
    """
    while True:
        print("Ha ha!")
    # end while
    return
# end def spam

class Class1:
    """A class with a single line `docstring`"""

    def __init__(self, param=None):
        """
        Initialize the class
        """
        self.param = param
    # end def

    def doit(self, param="Hello"):
        print("{!s} says {!s}".format(self.param, param))
        return
    # end def doit

# end class Class1

from . import submodule
from . import another

