
Command line usage
==================

Current command line usage is geared towards producing output suitable for
the `Casino <http://vallico.net/casinoqmc/>`_ Quantum Monte Carlo program. It
can readily be extended to output pseudopotentials in a different format.

The command structure is::

    $ gen_pseudo <type> [<args> ... ]

where ``<type>`` is one of ``troullier``, ``utp`` or ``swell``. A description
of the arguments for each pseudopotential can be obtained using::

    $ gen_pseudo help <type>

The command will produce a ``manual_interactions`` block suitable for
inclusion in the Casino input file. For instance::
    
    $ gen_pseudo troullier repulsive 1.0 1.0

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


We look at the arguments for each type of potential in more detail.

Troullier-Martins pseudopotentials
----------------------------------

To generate a pseudopotential following the Troullier-Martins form of
pseudopotentials, use one of the following commands::

    $ gen_pseudo troullier [--cutoff=<cutoff>] repulsive <a> <E>
    $ gen_pseudo troullier attractive <a> <E> <cutoff>
    $ gen_pseudo troullier bound <a> <cutoff>
    
We look at the arguments for each branch in detail.

Repulsive branch
++++++++++++++++

::

    $ gen_pseudo troullier repulsive <a> <E>

``<a>`` is the scattering length, ``<E>`` is the calibration energy. The cutoff is
calculated by default as the value of the first antinode of the true
wavefunction at incident energy ``E``. This can be altered by passing the
command line argument ``--cutoff=XX``::

    $ gen_pseudo --cutoff=XX repulsive <a> <E>

Attractive branch
+++++++++++++++++

::

    $ gen_pseudo troullier attractive <a> <E> <cutoff>

``<a>`` is the scattering length, ``<E>`` is the Fermi energy and
``<cutoff>`` is the cutoff, which must be smaller than the first node of the
wavefunction. 

Bound state
+++++++++++

::

    $ gen_pseudo troullier bound <a> <cutoff>

``<a>`` is the scattering length and ``<cutoff>`` is the cutoff, which must
be smaller than the first node of the wavefunction.

UTP pseudopotentials
--------------------

To generate a UTP, use one of::

    $ gen_pseudo utp [options] [--cutoff=<cutoff>] repulsive <a> <E>
    $ gen_pseudo utp [options] attractive <a> <E> <cutoff>

The arguments are identical to those for the relevant branch of the
Troullier-Martins potential. The optimizer will print convergence information
as it runs. This can be suppressed by passing ``--quiet`` or ``-q`` as an
option.

Square well pseudopotential
---------------------------

To generate a square well or top hat pseudopotential, use::

    $ gen_pseudo swell [--radius=<radius>] [--] <a>

where ``<a>`` is the scattering length, and ``--radius`` is the potential
radius. 

For repulsive potentials, if the radius is unspecified, the code will create a
pseudopotential with zero effective range. 

For attractive potential, the radius must be specified. To indicate a negative
scattering length, add a double dash ``--`` before the scattering length. For
instance, to create a square well with scattering length -0.5, use::

    $ gen_pseudo swell --radius=0.3 -- -0.5



Python API
==========

We expose a python API to make it easy to customise the output of ``contactpp``
or include it as part of other scripts. 

Importing ``contactpp`` exposes three functions:

 * ``contactpp.make_troullier_potential``

 * ``contactpp.make_utp_potential``

 * ``contactpp.make_square_well_potential``

See the API description below for details on the arguments to each of these
functions.

Each function returns a pseudopotential object. As an example of how to use
this object, we generate a Troullier-Martins pseudopotential and plot it using
matplotlib.

.. code-block:: python

    import contactpp
    import matplotlib.pyplot as plt
    import numpy as np

    pseudopotential = contactpp.make_troullier_potential(
            "repulsive",scattering_length=1.0,calibration_energy=1.0)

    print pseudopotential.cutoff
    # 1.8637284049928018

    print pseudopotential.coefficients
    # numpy array of coefficients.

    rs = np.linspace(0.,2*pseudopotential.cutoff)
    plt.plot(rs, pseudopotential.V(rs))
    plt.show()

Generating the pseudopotentials
-------------------------------

.. module:: contactpp

.. autofunction:: make_troullier_potential

.. autofunction:: make_utp_potential

.. autofunction:: make_square_well_potential

Pseudopotential objects
-----------------------

.. module:: contactpp.troullier

.. autoclass:: TroullierScatteringPotential

.. autoclass:: TroullierBoundPotential

.. module:: contactpp.utp

.. autoclass:: UTPPotential

.. module:: contactpp.swell

.. autoclass:: SquareWellPotential

