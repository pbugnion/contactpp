#!/usr/bin/env python
import os
import sys

DISTNAME = "contactpp"
DESCRIPTION = "Pseudopotential generator for the contact interaction"
MAINTAINER = "Pascal Bugnion"
MAINTAINER_EMAIL = "pascal@bugnion.org"
URL = "https://pypi.python.org/pypi/contactpp"
LICENSE = "new BSD"

LONG_DESCRIPTION = """

contactpp
=========

contactpp is a package for the generation of pseudopotentials for the 
contact interaction. The theory is outlined in [BNC]_. 


.. [BNC] P.O. Bugnion, R.J. Needs, and G.J. Conduit, 
         High-fidelity contact pseudopotentials and p-wave superconductivity.

Links
-----

* Home page: https://pypi.python.org/pypi/contactpp
* Documentation: http://contactpp.readthedocs.org/en/latest/
* Source code: https://github.com/pbugnion/contactpp
* Issues: https://github.com/pbugnion/contactpp/issues


Installation
------------

contactpp requires python2.7 and numpy. 

The easiest way to download and install ``contactpp`` is from the Python
package index. Run::

    $ python easy_install contactpp

This requires root access (unless you are running in a virtual environment).
To install without root access, run::

    $ python easy_install --user contactpp

To install from source, clone the git repository using::

    $ git clone https://github.com/pbugnion/contactpp.git

Navigate to the source's root directory (``contactpp``) and run::

    $ python setup.py install



Issue reporting and contributing
--------------------------------

Report issues using the `github issue tracker <https://github.com/scikit-monaco/scikit-monaco/issues>`_.

Read the CONTRIBUTING guide to learn how to contribute.
"""

if sys.version_info[0] < 3:
    import __builtin__ as builtins
else:
    import builtins

# This is a bit hackish: we are setting a global variable so that the main
# skmonaco __init__ can detect if it is being loaded by the setup routine, to
# avoid attempting to load components that aren't built yet. While ugly, it's
# a lot more robust than what was previously being used.
# Copied from scipy setup file.
builtins.__CONTACTPP_SETUP__ = True

def write_readme():
    """
    Create README file from LONG_DESCRIPTION, replacing non-standard
    bits of re-structured text.
    """
    with open("README.rst","w") as f:
        f.write("""\
.. Automatically generated from LONG_DESCRIPTION keyword in 
.. setup.py. Do not edit directly.\
""")
        f.write(LONG_DESCRIPTION.replace(".. code:: python","::"))

import contactpp

VERSION = contactpp.__version__


# For some commands, use setuptools.
if len(set(('develop', 'release', 'bdist_egg', 'bdist_rpm',
           'bdist_wininst', 'install_egg_info', 'build_sphinx',
           'egg_info', 'easy_install', 'upload',
           '--single-version-externally-managed',
            )).intersection(sys.argv)) > 0:
    import setuptools
    extra_setuptools_args = dict(
        zip_safe=False, # the package can run out of an .egg file
        include_package_data=True,
    )
else:
    extra_setuptools_args = dict()

def configuration(parent_package="",top_path=None):
    if os.path.exists("MANIFEST"):
        os.remove("MANIFEST")
    write_readme()
    from numpy.distutils.misc_util import Configuration
    config = Configuration(None,parent_package,top_path)

    # Avoid non-useful msg:
    # "Ignoring attempt to set 'name' (from ... "
    config.set_options(ignore_setup_xxx_py=True,
                       assume_default_configuration=True,
                       delegate_options_to_subpackages=True,
                       quiet=True)

    config.add_subpackage('contactpp')
    
    return config

def setup_package():
    metadata = dict(
            name=DISTNAME,
            maintainer=MAINTAINER,
            maintainer_email=MAINTAINER_EMAIL,
            description=DESCRIPTION,
            license=LICENSE,
            url=URL,
            version=VERSION,
            long_description=LONG_DESCRIPTION,
            scripts=["bin/gen_pseudo"],
            classifiers=[
                'Intended Audience :: Science/Research',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: BSD License',
                'Programming Language :: Python',
                'Topic :: Software Development',
                'Topic :: Scientific/Engineering',
                'Operating System :: POSIX',
                'Operating System :: Unix',
                'Operating System :: MacOS',
                'Programming Language :: Python :: 2',
                'Programming Language :: Python :: 2.7',
                ],
            **extra_setuptools_args)

    if (len(sys.argv) >= 2 and
            ("--help" in sys.argv[1:] or
             sys.argv[1] in ("--help-commands","egg_info","--version","clean"))):
        try:
            from setuptools import setup
        except ImportError:
            from distutils.core import setup

    else:
        from numpy.distutils.core import setup
        metadata["configuration"] = configuration
    setup(**metadata)

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup_package()
