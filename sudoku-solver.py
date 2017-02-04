from z3 import *

m = [[ Int("x_%s_%s" % (i+1, j+1))
       for j in range(9)] for i in range(9) ]

"""
Constraint definitions
"""
entryCnst  = [ And(1 <= m[i][j], m[i][j] <= 9)
               for i in range(9) for j in range(9) ]
rowCnst    = [ Distinct(m[i]) for i in range(9) ]
colCnst    = [ Distinct([ m[i][j] for i in range(9) ]) for j in range(9) ]
squareCnst = [ Distinct([ m[i + 3*p][j + 3*q]
                        for i in range(3) for j in range(3) ])
                        for p in range(3) for q in range(3) ]

constraint = entryCnst + rowCnst + colCnst + squareCnst

instance = ((0,0,0,0,9,4,0,3,0),
            (0,0,0,5,1,0,0,0,7),
            (0,8,9,0,0,0,0,4,0),
            (0,0,0,0,0,0,2,0,8),
            (0,6,0,2,0,1,0,5,0),
            (1,0,2,0,0,0,0,0,0),
            (0,7,0,0,0,0,5,2,0),
            (9,0,0,0,6,5,0,0,0),
            (0,4,0,9,7,0,0,0,0))

"""
(non-empty cell value) => (randomly generated variable valuations should match instance's non-empty values)
"""
instanceCnst = [ Implies(instance[i][j] != 0,
                         m[i][j] == instance[i][j])
                 for i in range(9) for j in range(9) ]

s = Solver();
s.add(constraint + instanceCnst);
if s.check() == sat:
    genInstance = s.model()     # Generated instance of sudoku
    genMatrix = [[ genInstance.evaluate(m[i][j]) for j in range(9) ]
                                                 for i in range(9) ]
    print_matrix(genMatrix)
else:
    print "Failed to solve!"
