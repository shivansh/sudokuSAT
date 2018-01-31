from z3 import *
import constraint as cnst
from random import randint

constraint = cnst.entryCnst + cnst.rowCnst + cnst.colCnst + cnst.squareCnst

# Precomputed 9x9 valid grid
genMatrix = [[4,9,1,6,7,3,2,5,8],
	     [2,5,3,9,8,1,4,6,7],
	     [6,7,8,4,5,2,9,3,1],
	     [9,3,5,7,2,6,8,1,4],
	     [7,1,4,8,3,9,6,2,5],
	     [8,6,2,5,1,4,3,7,9],
	     [3,2,7,1,9,8,5,4,6],
	     [1,4,9,2,6,5,7,8,3],
	     [5,8,6,3,4,7,1,9,2]]

# genMatrix will be manipulated, save it in refMat
refMat = [row[:] for row in genMatrix]

# TODO Fix this constraint
instanceCnst = [ Exists( [i,j],
                        And(genMatrix[i][j] != 0, genMatrix[i][j] != refMat[i][j]) )
                 for i in range(9) for j in range(9) ]

s = Solver();
s.add(constraint + instanceCnst)
for i in range(9):
    for j in range(9):
        print 'Iteration %s %s' % (i, j)
        if genMatrix[i][j] != 0:
            genMatrix[i][j] = 0
            if s.check() == sat:
                # Debug info
                print 'Cannot remove %s, %s' % (i, j)
                genMatrix[i][j] = refMat[i][j]

print_matrix(genMatrix)
