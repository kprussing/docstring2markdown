from setuptools import setup

import os
here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.markdown"), "r") as fid:
    long_desc=fid.read()

with open(os.path.join(here, "VERSION"), "r") as fid:
    version=fid.read().strip()

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

