
from numpy.testing import TestCase, run_module_suite

from contactpp.swell import bracket_root

def assert_inrange(x,(xlow,xhigh)):
    if xlow > xhigh:
        xlow, xhigh = xhigh, xlow
    assert xlow < x < xhigh

class TestBracketRoot(TestCase):

    def test_quadratic(self):
        """
        Bracket positive root in x^2 - 1
        """
        f = lambda x: x**2 - 1.
        brackets = bracket_root(f,0.)
        assert_inrange(1.,brackets)

    def test_exact_root(self):
        """
        Bracket positive root in x^2 - 1, falling exactly on root.
        """
        f = lambda x: x**2 - 1.
        brackets = bracket_root(f,0.,init_step=1.)
        assert_inrange(1.,brackets)
        assert brackets == (0.,2.)

    def test_quadratic_direction(self):
        """
        Bracket negative root in x^2 - 1.
        """
        f = lambda x: x**2 - 1.
        brackets = bracket_root(f,0.,direction=-1.)
        assert_inrange(-1.,brackets)


if __name__ == '__main__':
    run_module_suite()

