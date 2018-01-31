"""
Encoding for sudoku solving patterns.
"""

def scribble(k, xs):
    """Removes each occurrence of k in all the pencilled entires in list xs."""
    for x in xs:
        if isinstance(x, list) and len(x) > 1 and k in x:
            # If a pencilling is reduced to a single entry, it's already fixed.
            x.remove(k)

def crossout(mat):
    """Updates the pencilled entries by crossing out the irrelevant ones."""
    for row in mat:
        for j, x in enumerate(row):
            if not isinstance(x, list):  # not a pencilled entry
                # Remove instances of each fixed value from all the
                # pencilled ones in the corresponding row and column.
                scribble(x, row)
                scribble(x, [ r[j] for r in mat ])

    # Update pencilled entries within each 3x3 grid.
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            fixedvals = []
            # In the first pass across the grid, collect
            # all the fixed valued entries.
            for p in range(3):
                for q in range(3):
                    if not isinstance(mat[i+p][j+q], list):
                        # TODO handle single element lists
                        fixedvals.append(mat[i+p][j+q])
            # In the next pass, remove all the collected entries
            # (in the first pass) from the pencilled ones.
            for p in range(3):
                for q in range(3):
                    if isinstance(mat[i+p][j+q], list):
                        mat[i+p][j+q] = [ x for x in mat[i+p][j+q] \
                                            if x not in fixedvals ]

def last_in_box(mat):
    """Encoding for 'last remaining cell in a box' pattern."""

def last_in_row(mat):
    """Encoding for 'last remaining cell in a row' pattern."""

def last_in_col(mat):
    """Encoding for 'last remaining cell in a column' pattern."""

def prettyprint(mat):
    """Pretty-print the matrix."""
    s = [[str(e) for e in row] for row in mat]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print '\n'.join(table)

def main(mat):
    """Driver routine."""
    # Initialize empty cells as pencilled entries filled with all possibilities.
    mat = [ [ range(1, 10) if x == 0 else x for x in row ] for row in mat ]
    crossout(mat)
    prettyprint(mat)


mat = [[2,0,0,0,7,0,0,3,8],
       [0,0,0,0,0,6,0,7,0],
       [3,0,0,0,4,0,6,0,0],
       [0,0,8,0,2,0,7,0,0],
       [1,0,0,0,0,0,0,0,6],
       [0,0,7,0,3,0,4,0,0],
       [0,0,4,0,8,0,0,0,9],
       [8,6,0,4,0,0,0,0,0],
       [9,1,0,0,6,0,0,0,2]]
main(mat)
