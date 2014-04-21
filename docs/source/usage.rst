
Command line usage
==================

Current command line usage is geared towards producing output suitable for
the `Casino <http://vallico.net/casinoqmc/>`_ Quantum Monte Carlo program. It
can readily be extended to output pseudopotentials in a different format.

The command structure is::

    $ gen_pseudo [options] (repulsive|attractive|bound) <a> [other arguments]

Options must always appear straight after the program name. A reminder of the
arguments can be obtained by::

    $ gen_pseudo (-h|--help)

The command will produce a ``manual_interactions`` block suitable for
inclusion in the Casino input file::
    
    $ gen_pseudo repulsive 1.0 1.0

    %block manual_interaction
    polynomial
    order : 13
    cutoff : 1.4690133838
    c_0 : -6.68710073203
    c_1 : 0.0
    c_2 : 37.5550272665
    c_3 : 0.0
    c_4 : -76.8391296021
    c_5 : 11.4986279905
    c_6 : 86.9227576451
    c_7 : -14.7318519405
    c_8 : -74.7316666352
    c_9 : 28.0837647928
    c_10 : 29.2577382704
    c_11 : -21.989806382
    c_12 : 4.13182642699
    %endblock manual_interaction

We look at the arguments for each branch in more detail.

Repulsive branch
----------------

::

    $ gen_pseudo repulsive <a> <EF>

``<a>`` is the scattering length, ``<EF>`` is the Fermi energy. The cutoff is
calculated by default as the value of the first antinode of the true
wavefunction at incident energy ``EF``. This can be altered by passing the
command line argument ``--cutoff=XX``::

    $ gen_pseudo --cutoff=XX repulsive <a> <EF>

Attractive branch
-----------------

::

    $ gen_pseudo attractive <a> <EF> <cutoff>

``<a>`` is the scattering length, ``<EF>`` is the Fermi energy and
``<cutoff>`` is the cutoff, which must be smaller than the first node of the
wavefunction. 

Bound state
-----------

::

    $ gen_pseudo bound <a> <cutoff>

``<a>`` is the scattering length and ``<cutoff>`` is the cutoff, which must
be smaller than the first node of the wavefunction.


Python API
==========

We expose a python API to make it easy to customise the output of ``contactpp`` or include it as part of other scripts. The following example
plots the potential using matplotlib.

.. code-block:: python

    import contactpp
    import matplotlib.pyplot as plt
    import numpy as np

    pseudopotential = contactpp.make_troullier_potential(
            "repulsive",scattering_length=1.0,calibration_energy=1.0)

    print pseudopotential.cutoff
    # 1.4690133838031225

    print pseudopotential.coefficients
    # [ -6.68710073   0.          37.55502727   0.         -76.8391296
    # 11.49862799  86.92275765 -14.73185194 -74.73166664  28.08376479
    # 29.25773827 -21.98980638   4.13182643]

    rs = np.linspace(0.,2*pseudopotential.cutoff)
    plt.plot(rs, pseudopotential.V(rs))
    plt.show()

Generating the pseudopotential
------------------------------

.. module:: contactpp

.. autofunction:: make_troullier_potential

Pseudopotential objects
-----------------------

.. autoclass:: TroullierScatteringPotential

.. autoclass:: TroullierBoundPotential

