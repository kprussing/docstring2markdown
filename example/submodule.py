__doc__="""
A submodule to ensure we can get the `docstring`s from submodules.
There is no real data here.  I'm just adding arbitrary stuff to ensure
that I get it correct.

"""

class Class2:
    """
    A class defined in the submodule.

    """

    def __init__(self, param):
        """
        Initialize Class2

        Yeah, this doesn't really do anything.  But wait!  Here's some
        math
        $$
            E = mc^2
        $$
        and a code block

            >>> print('Hi!')
            Hi!

        And you cannot neglect in-line math $X=Y$.

        """
        return
    # end def __init__

    def doit(self, param):
        """
        Test the required parameter.

        This is a method call to check a required parameter.  The class
        methods will wind up being level 3 headers so use level 4 for
        the parameters.

        ##### Parameters

        param : [*scalar*]
            You must pass a scalar value.

        ##### Returns

        out : [*scalar*]
            1

        """
        self.param = param
        return 1
    # end def doit

def eggs(inp, keyword="$E=mc^2$"):
    """
    Spam the output with a keyword argument

    Write given keyword argument to the input forever.  Module level
    functions map to level 2 headers meaning parameters should be level
    3.

    ### Parameters

    inp : [*scalar*]
        Something initially printed to the screen
    keyword : [*string*]
        Print this forever

    """
    print("Input was {!s}".format(inp))
    while True:
        print(keyword)
    # end while
    return
# end def eggs

