from z3 import *
from random import randint

# Input variable matrix
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

instanceCnst = [ Implies(genMatrix[i][j] != '@',
                         m[i][j] == genMatrix[i][j])
                 for i in range(9) for j in range(9) ]

s = Solver();
s.add(constraint + instanceCnst)
while True:
    # Select random i, j for removal and check if unique solution exists
    i = randint(0,8)
    j = randint(0,8)
    if genMatrix[i][j] != '@':
        genMatrix[i][j] = '@'
        if s.check() == sat:
            model = s.model()
            genSoln = [[ model.evaluate(m[p][q]) for q in range(9) ]
                                                 for p in range(9) ]
            # If generated soln != ref matrix, no more unique soln are possible
            if genSoln != refMat:
                print "No more unique solution exist!"
                break

# Fill back the value at index (i,j)
genMatrix[i][j] = refMat[i][j]
print_matrix(genMatrix)
