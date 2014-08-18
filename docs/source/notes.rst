
Release notes
-------------

1.1
^^^

When making UTP potentials, the Python API allows the user to choose an
objective function that minimizes the maximum error in phase shift, rather than
minimizing the RMS error.

1.0.3
^^^^^

Initial public tested release. `contactpp` can generate:

 * Square well and top hat pseudopotentials,
 * Troullier-Martins pseudopotentials,
 * UTP pseudopotentials.

This program provides a command line script that produces input suitable for
inclusion in a `Casino <http://vallico.net/casinoqmc/>`_ input file, and a
Python API.
