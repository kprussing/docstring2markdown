`docstring2markdown`
====================

Convert the `docstring`s of a Python package into Markdown.

This is tool I developed while working on my dissertation.  I needed a
way to convert the `docstring`s in my Python package into a usable API
that I could include in the appendix.  Technically,
[Sphinx][Sphinx] is the way to do this.  However, I ran
into two main problems:

1.  I know [Markdown][Markdown] and not reStructuredText and do not have
    the desire to learn yet another markup language.  Also, I really
    think [CommonMark][CommonMark] will be good for the community as a
    whole and the more people who use it the better.
2.  I don't like the HTML output of Sphinx and could not extract the 
    LaTeX output to include in my dissertation.

My primary goals for this tool are:

1.  Let me write my `docstring`s in Markdown.
2.  Generate a sane Markdown output that [`pandoc`][pandoc] can convert
    to LaTeX.
3.  Get something that looks as good as the output of the `help`
    function provided by the `pydoc` module inside of Python.

With this in mind, I set out to make a usable tool for myself.
Ultimately, I don't really care what flavor of markup language the
`docstring` uses.  I just want to get the documentation and write it in
a sane manner to the standard output.

A few comments on how it works.  First, I will use the ATX style headers
to section parts off.  *All* modules will be level 1 headers which
`pandoc` maps to `\section`.  Classes will be set as level 2 headers
under the module.  Functions offer a bit of a challenge.  Functions
defined at the module level need to be level 2 headers while class
methods need to be level 3 under the correct class.  

A second point is handling the parameters.  Ideally, these would be
marked as level 3 or level 4 by the documenter.  I might want to inject
extra `#`s on the fly.  We could always let the documenter write the
parameters as level 1 headers because in the scope of the function this
is true.  We could then inject the function's `##` or `###` dynamically.

An example module is provided for testing purposes.

[Markdown]: http://daringfireball.net/projects/markdown/syntax
[Sphinx]: http://sphix-doc.org
[CommonMark]: http://commonmark.org
[pandoc]: http://johnmacfarlane.net/pandoc/


Installation
------------

The usual suspect of:

    $ python setup.py install

Usage
-----

Run

    $ docstring2markdown module

and the `docstring`s will be extracted and printed to standard out.

Future Improvements
-------------------

1.  Rigorously test the routine.  Currently, it works for me and my
    dissertation work.
2.  Possibly integrate dynamic documenting.  Most likely this will not
    happen because [Sphinx][sphinx] is the correct way to generate
    Python documentation.

License
-------

Copyright (c) 2014, Keith F Prussing
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright
  notice, this list of conditions and the following disclaimer in the
  documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

