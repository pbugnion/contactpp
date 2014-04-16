
import sys

def print_for_casino(pseudopotential,stream=sys.stdout):
    stream.write("%block manual_interaction\n")
    stream.write("polynomial\n")
    stream.write("order : {}\n".format(len(pseudopotential.coefficients-1)))
    stream.write("cutoff : {}\n".format(pseudopotential.cutoff))
    for icoeff, coeff in enumerate(pseudopotential.coefficients):
        stream.write("c_{} : {}\n".format(icoeff,coeff))
    stream.write("%endblock manual_interaction\n")

