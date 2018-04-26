def set_difference(l1, l2):
    return [x for x in l1 if x not in l2]

def intersection(l1, l2):
    return [x for x in l1 if x in l2]

def union(l1, l2):
    return intersection(l1, l2) + symmetric_difference(l1, l2)

def symmetric_difference(l1, l2):
    return [x for x in l1+l2 if x not in intersection(l1, l2)]

def cartesian_product(l1, l2):
    return [(x, y) for x in l1 for y in l2]

