"""
Constraint definitions
"""

from z3 import *

# Input variable matrix
m = [[ Int("x_%s_%s" % (i+1, j+1))
       for j in range(9)] for i in range(9) ]

entryCnst  = [ And(1 <= m[i][j], m[i][j] <= 9)
               for i in range(9) for j in range(9) ]
rowCnst    = [ Distinct(m[i]) for i in range(9) ]
colCnst    = [ Distinct([ m[i][j] for i in range(9) ]) for j in range(9) ]
squareCnst = [ Distinct([ m[i + 3*p][j + 3*q]
                        for i in range(3) for j in range(3) ])
                        for p in range(3) for q in range(3) ]
