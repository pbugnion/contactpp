
from numpy.testing import TestCase, assert_allclose, run_module_suite

import contactpp

class TestTroullierRepulsiveGenerator(TestCase):

    def test_simple(self):
        """
        Repulsive, k = 1.0, a = 0.5, default cutoff.
        """
        pseudo = contactpp.TroullierRepulsiveGenerator(0.5,1.0).\
                make_pseudopotential()
        assert_allclose(pseudo.cutoff, 1.4213277165)
        true_coeffs = [ 1.43297755,  0.,  0.10274265, 0., -1.64351441,
        0.9249928 , -0.28740129,  0.14383292,  0.01680047, -0.00838876,
        0.1072442 , -0.10709773,  0.02673786]
        true_coeffs = [ 2.86595509133, 0.0, 0.205485304827, 0.0, 
                -3.28702881566, 1.849985596783, -0.574802579255, 
                0.2876658369341, 0.033600944008, -0.01677752615456, 
                0.2144884097068, -0.214195464437, 0.0534757298172 ]
        assert_allclose(pseudo.coefficients,true_coeffs,rtol=1e-6)


class TestTroullierAttractiveGenerator(TestCase):

    def test_simple(self):
        """
        Attractive, k = 1.0, a = -0.5, c = 0.5
        """
        pseudo = contactpp.TroullierAttractiveGenerator(-0.5,1.0,0.5).\
                make_pseudopotential()
        assert pseudo.cutoff == 0.5
        true_coeffs = [-82.610856869, 0.0, 2266.56108128, 0.0, -28066.2678240, 
            13585.9883237, 180018.229885, -94661.343764, -975417.06523, 
            1012025.88164, 2679168.07963, -5559442.2826, 2884048.105220]
        assert_allclose(pseudo.coefficients,true_coeffs)


class TestTroullierBoundGenerator(TestCase):

    def test_simple(self):
        """
        Bound, a = 1.0, c = 0.5
        """
        pseudo = contactpp.TroullierBoundGenerator(1.0,0.5).\
                make_pseudopotential()
        assert pseudo.cutoff == 0.5
        true_coeffs = [-146.841892049, 0.0, 4886.5919754, 0.0, -68143.190035, 
                22804.9105464, 519357.563365, -278109.479783, -2754186.70635,
                2858643.479, 7542990.09993, -15658139.2347, 8125999.14114]
        assert_allclose(pseudo.coefficients,true_coeffs)



if __name__ == "__main__":
    run_module_suite()



