"""
Grammar definitions
"""

def row(mat, i, k):
    """Returns true if the i'th row contains k"""
    if k in mat[i]:
        return True
    return False

def col(mat, i, k):
    """Returns true if the i'th column contains k"""
    if k in [row[i] for row in mat]:
        return True
    return False

def grid(mat, i, j, k):
    """Returns true if the specified grid contains k"""
    if k in [ mat[i + p][j + q] for p in range(3) for q in range(3) ]:
        return True
    return False
