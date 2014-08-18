
Installation
============

Requirements
------------

python2.7, numpy, scipy. These can be installed on a Debian system using::

    $ sudo apt-get install python-numpy python-scipy

The easy way
------------

The easiest way to download and install ``contactpp`` is from the Python
package index. Run::

    $ easy_install contactpp

This requires root access (unless you are running in a virtual environment).
To install without root access, run::

    $ easy_install --user contactpp


From github
-----------

Clone the git repository using::

    $ git clone https://github.com/pbugnion/contactpp.git

Navigate to the source's root directory (``contactpp``) and run::

    $ python setup.py install

From source
-----------

If you have a *.zip or *.tar.gz archive with the source, unpack the archive
in a directory, navigate into this directory and run::

    $ python setup.py install
