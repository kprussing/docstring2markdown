from setuptools import setup
from docstring2markdown import __version__ as version

import os
here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.markdown"), "r") as fid:
    long_desc=fid.read()

setup(
        name="docstring2markdown",
        version=version,
        long_description=long_desc,
        entry_points={
            "console_scripts" : [
                    "docstring2markdown=docstring2markdown:main"
                ]
            }
    )

