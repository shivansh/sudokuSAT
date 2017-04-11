from z3 import *
import constraint as cnst

# Input variable matrix
m = [[ Int("x_%s_%s" % (i+1, j+1))
       for j in range(9)] for i in range(9) ]

constraint = cnst.entryCnst + cnst.rowCnst + cnst.colCnst + cnst.squareCnst

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
