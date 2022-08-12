import sympy
from einsteinpy.symbolic import ChristoffelSymbols, RiemannCurvatureTensor
from einsteinpy.symbolic.predefined import Schwarzschild

sympy.init_printing()


sw = Schwarzschild()
sw.tensor()
