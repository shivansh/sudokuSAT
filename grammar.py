"""
Grammar definitions
"""

def lookup(k, l):
    """
    lookup k in a list l, which can also have pencilled entries. A
    pencilled entry is a list of possible values a cell might contain.
    """
    for elem in l:
        if isinstance(elem, list):  # pencilled entry
            for x in elem:
                if x == k:
                    return True
        elif elem == k:
            return True
    return False

def row(mat, i, k):
    """Returns true if the i'th row contains k"""
    return lookup(k, mat[i])

def col(mat, i, k):
    """Returns true if the i'th column contains k"""
    return lookup(k, [row[i] for row in mat])

def grid(mat, i, j, k):
    """Returns true if the specified grid contains k"""
    return lookup(k, [ mat[i + p][j + q] for p in range(3) for q in range(3) ])
