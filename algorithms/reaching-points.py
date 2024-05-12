# Given four integers sx, sy, tx, and ty,
# return true if it is possible
# to convert the point (sx, sy) to the point (tx, ty) through some operations,
# or false otherwise.
# The allowed operation on some point (x, y)
# is to convert it to either (x, x + y) or (x + y, y).

def reaching_points(sx, sy, tx, ty):
    while tx >= sx and ty >= sy:
        if sx == tx and sy == ty:
            return True
        if tx > ty:
            tx -= ty
        else:
            ty -= tx
    return False

# Time: O(max(tx,ty)), if ty = 1, we could be subtracting tx times
# Space: O(1)


def reaching_points(sx, sy, tx, ty):
    while tx >= sx and ty >= sy:
        if tx == ty:
            break
        elif tx > ty:
            if ty > sy:
                tx %= ty
            else:
                return (tx - sx) % ty == 0
        else:
            if tx > sx:
                ty %= tx
            else:
                return (ty - sy) % tx == 0
    return tx == sx and ty == sy

# Time: O(log(max(tx,ty))), assuming that the mod operation can be done in
# O(1) time
# Space: O(1)
