
def cross(A, B):
    return [a+b for a in A for b in B]


digits   = '123456789'
rows     = 'ABCDEFGHI'
cols     = digits

squares  = cross(rows, cols)

rows_units = [cross(r, cols) for r in rows]
cols_units = [cross(rows, c) for c in cols]
squares_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]

unitlist = rows_units + cols_units + squares_units

units = {s: [u for u in unitlist if s in u] for s in squares}
