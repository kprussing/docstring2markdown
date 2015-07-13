__doc__="""
Parse a Python package and print the `docstring`s to standard output.

Given a Python package, recurse down to find all of the `docstring`s in
the submodules, classes, and functions and print them to the standard
output.  Print the `docstring`s as written and do *not* attempt to apply
additional formatting.  In the case of classes or functions, print the
first line description as a level 3 header so that the user knows what
the object is.

The package is imported at runtime, so it had better be a valid package.

"""
import logging
import os
import pkg_resources
import pydoc

__version__ = pkg_resources.get_distribution(
        os.path.split(os.path.dirname(__file__))[1]
    ).version

logging.getLogger(__name__).addHandler(logging.NullHandler())

def document(obj, level="#"):
    """
    Extract the documentation for an object.

    Extract the `docstring` for the given object.  The object must be
    loaded at call time.  If the object is a module and module
    recognized as a package, recurse down each submodule.  All classes
    and functions are listed before the submodule members.  Return a
    string with of the documentation.

    ### Parameters

    obj : [*object*]
        The object to document.
    level : [*string*]
        The ATX header to prepend the object name.  Default is '#'.

    """
    logger = logging.getLogger(__name__ +".document")
    logger.info("Process {:s}".format(obj.__name__))
    doc = level +" " +obj.__name__
    #
    if pydoc.inspect.isfunction(obj):
        argspec = pydoc.inspect.getfullargspec(obj)
        args = []
        for it in range(len(argspec.args)):
            args.append(argspec.args[it])
            if argspec.defaults:
                if (len(argspec.args) -it) <= len(argspec.defaults):
                    args[-1] += "={!s}".format(
                            argspec.defaults[len(argspec.args) -it -1]
                        )
                # end if
            # end if
        # for
        doc += "({:s})".format(", ".join(args))
    # end if
    doc += os.linesep.join(["", "", pydoc.getdoc(obj), ""])
    #
    if pydoc.inspect.isfunction(obj):
        # Do not recurse down functions.
        return doc
    # end if
    #
    logger.debug("    Inspect the object for members")
    classes = {}
    functions = {}
    modules = {}
    fname = pydoc.inspect.getabsfile(obj)
    for key, val in pydoc.inspect.getmembers(obj):
        if key[0] == "_":
            # Do _not_ handle 'private' members.
            continue
        # end if
        if pydoc.inspect.isfunction(val):
            if pydoc.inspect.getabsfile(val) == fname:
                functions.update({key : val})
            # end if
        elif pydoc.inspect.isclass(val):
            # The __class__ object is a false alarm.
            if key == "__class__":
                classes.update({key : val})
            # end if
        elif pydoc.inspect.ismodule(val):
            # If it's not a submodule, skip it.
            if obj.__name__ in val.__name__:
                modules.update({key : val})
            # end if
        # end if
    # end for
    #
    if classes:
        logger.debug("Classes   : {!s}".format(classes))
        for key in sorted(list(classes.keys())):
            doc += os.linesep +document(classes[key], "##")
        # end for
    # end if
    #
    if functions:
        logger.debug("Functions : {!s}".format(functions))
        for key in sorted(list(functions.keys())):
            doc += os.linesep +document(functions[key], level +"#")
        # end for
    # end if
    #
    if modules:
        logger.debug("Modules   : {!s}".format(modules))
        for key in sorted(list(modules.keys())):
            doc += os.linesep +document(modules[key], "#")
        # end for
    # end if
    #
    return doc
# end def document_module

def main():
    """The main routine"""
    import argparse
    import importlib
    import sys
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("PACKAGE", help="The package to parse")
    #
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--verbose", "-v", action="store_true")
    group.add_argument("--debug", "-d", action="store_true")
    #
    args = parser.parse_args()
    if args.debug:
        level = logging.DEBUG
    elif args.verbose:
        level = logging.INFO
    else:
        level = logging.WARNING
    # end if
    logging.basicConfig(level=level)
    #
    try:
        pkg = importlib.import_module(args.PACKAGE)
        res = document(pkg)
        print(res)
    except ImportError as err:
        logging.error("{!s}".format(err))
        sys.exit(1)
    except RuntimeError as err:
        logging.error("Oh no! {!s}".format(err))
        sys.exit(2)
    # end try
    #
    sys.exit()
    return
# end def main

if __name__ == "__main__":
    main()
# end if

